import math
import random
from typing import List


class Chromosome:
    def __init__(self, x: float, y: float):
        # assert -60 <= x <= 40, f"x can't be: {x}"
        # assert -30 <= y <= 70, f"y can't be: {y}"
        self.x = x
        self.y = y

    def f(self):
        x = abs(self.x)
        y = abs(self.y)
        return (x+y)*(1+abs(math.sin(x*math.pi)) + abs(math.sin(y*math.pi)))

    def fittness(self):
        t = 400-self.f()
        if t < 0:
            print("DEBUG:", "SIAAAAVAAAASHHHH....")
        return t

    def __str__(self):
        return f"Chromosome ({self.x}, {self.y})"

    __repr__ = __str__

    def crossover(self, other, l1, l2):
        assert l1 + l2 == 1, f"What??? {l1} + {l2} is not 1"
        x1 = l1*self.x + l2*other.x
        y1 = l1*self.y + l2*other.y
        child1 = Chromosome(x1, y1)
        x2 = l2*self.x + l1*other.x
        y2 = l2*self.y + l1*other.y
        child2 = Chromosome(x2, y2)
        return child1, child2

    def copy(self):
        return Chromosome(self.x, self.y)

    def does_violate(self):
        if -60 <= self.x <= 40 and -30 <= self.y <= 70:
            return False
        return True

    def mutate(self):
        range_ = 4
        epsilon_x = random.uniform(-range_, range_)
        epsilon_y = random.uniform(-range_, range_)
        self.x += epsilon_x
        self.y += epsilon_y
        while self.does_violate():
            self.x -= epsilon_x
            self.y -= epsilon_y
            epsilon_x = random.uniform(-range_, range_)
            epsilon_y = random.uniform(-range_, range_)
            self.x += epsilon_x
            self.y += epsilon_y


class Genetic0012:
    def __init__(self, output_count: int, population_size: int,
                 generation_count: int, pc: float, pm: float):
        self.l2 = 0.7
        self.l1 = 0.3
        self.pc = pc
        self.pm = pm
        self.N = population_size
        self.T = generation_count
        self.output_count = output_count
        self.population: List[Chromosome] = []
        self.k = 3

    def _create_initial_population(self):
        for _ in range(self.N):
            c = Chromosome(
                x=random.uniform(-60, 40),
                y=random.uniform(-30, 70)
            )
            self.population.append(c)

    def parent_selection(self):
        # Tournament
        mating_pool = []
        for _ in range(self.N):
            lst = []
            for _ in range(self.k):
                lst.append(random.choice(self.population))
            c = max(lst, key=lambda e: e.fittness())
            mating_pool.append(c)
        return mating_pool

    def crossover(self, mating_pool: List[Chromosome]):
        off_springs = []
        while mating_pool:
            p1 = random.choice(mating_pool)
            mating_pool.remove(p1)
            p2 = random.choice(mating_pool)
            mating_pool.remove(p2)
            if random.random() < self.pc:
                c1, c2 = p1.crossover(p2, self.l1, self.l2)
                if c1.does_violate():
                    off_springs.append(p1)
                else:
                    off_springs.append(c1)
                if c2.does_violate():
                    off_springs.append(p2)
                else:
                    off_springs.append(c2)
            else:
                off_springs.append(p1)
                off_springs.append(p2)
        return off_springs

    def mutation(self, off_spring: List[Chromosome]):
        for chromosome in off_spring:
            if random.random() < self.pm:
                chromosome.mutate()

    def run(self):
        self._create_initial_population()
        pass
