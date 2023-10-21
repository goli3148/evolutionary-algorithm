from .Individual import Individual
from typing import List, Tuple, Dict
import random


class Population():
    
    GeneSize:int 
    NucleotideDomain = []
    
    FixedPopulationSize: int
    PopulationSize:int
    
    Individuals: List[Individual] = []
    Parents: List[Tuple[Individual, Individual]] = []
    
    def __init__(self, geneSize, nucleotideDomain, FixedpopulationSize) -> None:
        self.GeneSize = geneSize
        self.NucleotideDomain = nucleotideDomain
        self.FixedPopulationSize = self.PopulationSize = FixedpopulationSize
        for index in range(self.FixedPopulationSize):
            self.Individuals.append(Individual(geneSize, nucleotideDomain, index, randomCreation=True))
            
    def createRandomParents(self):
        self.Parents = []
        for i in range(0, self.PopulationSize, 2):
            if i+1 >= self.PopulationSize: 
                self.Parents.append((self.Individuals[i], self.Individuals[i]))
                self.Individuals[i].Parenting=True
            else: 
                self.Parents.append((self.Individuals[i], self.Individuals[i+1]))
                self.Individuals[i].Parenting = True
                self.Individuals[i+1].Parenting = True
    
    def randomDeath(self, num=4):
        for _ in range(num): 
            self.Individuals.pop(random.randint(0, self.PopulationSize-1))
            self.updatePopulationSize()
    
    def evaluationDeath(self, id):
        for index in range(self.PopulationSize):
            if index >= self.PopulationSize: break
            if id == self.Individuals[index].ID:
                self.Individuals.pop(index)
                self.updatePopulationSize()
                break
    
    def mutation(self, num=4):
        for _ in range(num): 
            parentin = True
            randomIndividualIndex = -1
            while parentin:
                randomIndividualIndex = random.randint(0, self.PopulationSize-1)
                parentin = self.Individuals[randomIndividualIndex].Parenting
            self.Individuals[randomIndividualIndex].mutation()
    
    # CROSS OVER PART
    Crossovers: Dict[int, str] = {1:'singlepoint', 2:'twopoint', 3:'uniform'}
    def crossover(self, parent: Tuple[Individual, Individual], crossoverType: int=None, randomSel:bool=True):
        crossoverType = random.choice(list(self.Crossovers.keys())) if randomSel else crossoverType
        NewGene = []
        if crossoverType == 1:
            jointPoint = random.randint(0, self.GeneSize-1)
            copy1 = parent[0].GeneCode[:jointPoint]
            copy2 = parent[1].GeneCode[jointPoint:]
            NewGene = copy1 + copy2
        elif crossoverType == 2:
            jointPoint1 = random.randint(0, self.GeneSize-1)
            jointPoint2 = random.randint(0, self.GeneSize-1)
            (jointPoint1, jointPoint2) = (jointPoint1, jointPoint2) if jointPoint1 < jointPoint2 else (jointPoint2, jointPoint1)
            copy1 = parent[0].GeneCode[jointPoint1:jointPoint2]
            NewGene = parent[1].GeneCode[:jointPoint1] + copy1 + parent[1].GeneCode[jointPoint2:]
        elif crossoverType == 3:
            NewGene = parent[0].GeneCode
            for index in range(len(NewGene)):
                if random.random() < 0.5:
                    NewGene[index] = parent[1].GeneCode[index]
        self.Individuals.append(Individual(self.GeneSize, self.NucleotideDomain,self.Individuals[-1].ID+1, NewGene, False))
        self.updatePopulationSize()
    
    def updatePopulationSize(self):
        self.PopulationSize = len(self.Individuals)
            

            



#pop = Population(8, [0,1], 20)
# pop.createRandomParents()
# for p in pop.Parents:
#     print(f"{p[0].ID}:{p[0].GeneCode},\t{p[1].ID}:{p[1].GeneCode}", end='\n')
# print("mut test")
# print(pop.Individuals[0].GeneCode)
# pop.Individuals[0].mutation(3,False)
# print(pop.Individuals[0].GeneCode)
# print("del test")
# for ind in pop.Individuals:
#     print(ind.ID, end='\t')
# print()
# pop.randomDeath(2)
# for ind in pop.Individuals:
#     print(ind.ID, end='\t')
# pop.evaluationDeath(4)
# for ind in pop.Individuals:
#     print(ind.ID, end='\t')
