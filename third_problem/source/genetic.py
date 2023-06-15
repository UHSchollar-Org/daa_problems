from typing import List
from utils import parse_formula
import random as rnd

class Genetic:
    def __init__(self, generations : int, individuals : int, mutation_rate : float) -> None:
        self.generations = generations
        self.individuals = individuals
        self.mutation_rate = mutation_rate
    
    def Solve(self, n, m, c):
        formula = parse_formula(c)
        
        population = self.create_population(n)
        
        for _ in range(self.generations):
            selection = self.selection(population, formula)
            if self.fitness(selection[0], formula) == m:
                return selection[0]
            population = self.breed(selection)

        population = self.selection(population, formula)
        return population[0]

    def create_population(self, n) -> List[List[int]]:
        population : List[List[int]] = []
        
        for _ in range(self.individuals):
            population.append(self.create_individual(n))
        
        return population

    def create_individual(self, n):
        individual : List[int] = []
        
        for _ in range(n):
            individual.append(rnd.randint(0,1))
        
        return individual

    def selection(self, population, c):
        selection = [(individual, self.fitness(individual, c)) for individual in population]
        selection = [individual for individual in sorted(selection, key=lambda x: x[1], reverse=True)]
        selection = selection[:self.individuals//2]
        selection = [individual[0] for individual in selection]
        return selection

    def fitness(self, individual, c) -> float:
        fitness = 0
        for clause in c:
            fitness += self.evaluate(individual, clause)
        return fitness

    def evaluate(self, individual, clause) -> int:
        for variable in clause:
            literal = abs(int(variable))
            if variable[0] == '-':
                if individual[literal - 1] == 0:
                    return 1
            else:
                if individual[literal - 1] == 1:
                    return 1
        return 0

    def breed(self, selection):
        population = self.crossover(selection)
        population = self.mutation(population)
        return population

    def crossover(self, selection):
        new_population = []
        for i in range(len(selection)//2):
            new_population.append(self.merge(selection[i], selection[len(selection)-i-1]))
        for i in range(0, len(selection)-1, 2):
            new_population.append(self.merge(selection[i], selection[i+1]))
        new_population = new_population + selection
        return new_population

    def merge(self, individual1, individual2):
        new_individual = []
        for i in range(len(individual1)):
            if i%2 == 0:
                new_individual.append(individual2[i])
            else:
                new_individual.append(individual1[i])
        return new_individual

    def mutation(self, population):
        for i in range(len(population)):
            population[i] = self.mutate(population[i])
        return population

    def mutate(self, individual):
        if rnd.random() < self.mutation_rate:
            index = rnd.randint(0,len(individual)-1)
            individual[index] = (individual[index] + 1) % 2
        return individual