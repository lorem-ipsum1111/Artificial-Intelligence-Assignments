import random
import copy
import math
import numpy as np


#this function calculates number of attacking pairs
def fitness(individual):
    

def crossover(individual1, individual2):
    


def mutation(individual):
    

def generate_individual(n):
    result = list(range(1, n + 1))
    np.random.shuffle(result)
    return result

class Genetic(object):

    def __init__(self, n ,pop_size):
        #initializing a random individuals with size of initial population entered by user
        self.queens = []
        for i in range(pop_size):
            self.queens.append(generate_individual(n))

    #generating individuals for a single iteration of algorithm
    def generate_population(self, random_selections=5):
        candid_parents = []
        candid_fitness = []
        #getting individuals from queens randomly for an iteration
        for i in range(random_selections):
            candid_parents.append(self.queens[random.randint(0, len(self.queens) - 1)])
            candid_fitness.append(fitness(candid_parents[i]))
        sorted_fitness = copy.deepcopy(candid_fitness)
        #sort the fitnesses of individuals
        
        #getting 2 first individuals(min attackings)
        
        #crossover the two parents
        
        # mutation
        
        #in code below check if each child is better than each one of queens individuals, set that individual the new child
        

    def finished(self):
        for i in self.queens:
            #we check if for each queen there is no attacking(cause this algorithm should work for n queen,
            # it was easier to use attacking pairs for fitness instead of non-attacking)
            

    def start(self, random_selections=5):
        #generate new population and start algorithm until number of attacking pairs is zero
        while not self.finished()[0]:
            self.generate_population(random_selections)
        final_state = self.finished()
        print(('Solution : ' + str(final_state[1])))


******************** N-Queen Problem With GA Algorithm ***********************

n=(int)(input('Enter the value of N \n -'))
initial_population=(int)(input('Enter initial population size \n -'))

algorithm = Genetic(n=n,pop_size=initial_population)
algorithm.start()
