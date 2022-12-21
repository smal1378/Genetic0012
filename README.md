
# GENETIC0012
A genetic algorithm for solving a continuous variable optimization.

### Target Function
Find `(x, y)` where below function is minimum on.
f(x, y) = (|x|+|y|).(1+|sin(|x|.𝜋)| + |sin(|y|.𝜋)|)
-60 <= x <= 40
-30 <= y <= 70
=> minimum f(x, y) is zero
### Why this name?
Genetic0012, well that name just come to my mind!

### Algorithm Type:
Haghighi

### Chromosome:
(x, y)

### Steps:
1 - Chromosome
2 - Initial Population
3 - Parent Selection - Tournament with dynamic k
4 - CrossOver
5 - Mutation
### Todo
6 - Survive Selection
7 - Stop If
8 - Return k fittest
