import math
import numpy
from matplotlib import pyplot

from genetic0012 import Genetic0012

g = Genetic0012(5, 10, 100, 0.1, 0.1)
g.run()
print(*g.population, sep='\n')
print("------- Mating Pool:")
mating_pool = g.parent_selection()
print(*mating_pool, sep='\n')
off_spring = g.crossover(mating_pool)
print("------ Off Spring:")
print(*off_spring, sep='\n')
print("------ Mutate:")
g.mutation(off_spring)
print(*off_spring, sep='\n')

# x = [c.x for c in g.population]
# y = [c.y for c in g.population]
# z = [c.f() for c in g.population]

# print(x, y , z, sep='\n')

# points3d(x, y, z)
# pyplot.show()


x = numpy.linspace(-60, 40, 300)
y = numpy.linspace(-30, 70, 300)

X, Y = numpy.meshgrid(x, y)


# def f(x, y):
#     x = abs(x)
#     y = abs(y)
#     return (x + y) * (1 + abs(math.sin(x * math.pi)) + abs(math.sin(y * math.pi)))
#
# Z = f(X, Y)

