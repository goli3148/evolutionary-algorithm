from .Population import Population
from typing import List, Dict
from .Gene import Gene
class EA():
    GENESIZE = 8
    NUECLOETIDEDOMAIN = [0,1]
    POPULATIONSIZE = 16
    EVALUATEDELETESIZE = 4
    RANDOMDELETESIZE = 4
    MUTATIONSIZE = 4
    REPEATLOOP = 50
    POPULATIONCROSSOVERS = 4
    
    population: Population
    
    DataSamplingIndex: int = 0
    DataSampling: List[List[Gene.Nucleotide]] = [[]]
    
    
    def __init__(self) -> None:
        self.population = Population(FixedpopulationSize=self.POPULATIONSIZE, geneSize=self.GENESIZE, nucleotideDomain=self.NUECLOETIDEDOMAIN)
    
    def run(self):
        self.startFunc()
        # Fist Run
        self.loopFunc()
        self.Enviroment()
        self.Selection()
        for rep in range(self.REPEATLOOP):
            self.CrossOver()
            self.loopFunc()
            if rep+2 == self.REPEATLOOP:
                break
            self.Mutation()
            self.Enviroment()
            self.Selection()
        self.endFunc()
        ...
        
    def Selection(self):
        self.population.createRandomParents()
        
    def CrossOver(self):
        rep = int(self.POPULATIONCROSSOVERS / len(self.population.Parents))
        for _ in range(rep):
            for j in range(len(self.population.Parents)): 
                self.population.crossover(self.population.Parents[j])
        
    def Mutation(self):
        self.population.mutation(self.MUTATIONSIZE)
        ...
        
    def Evaluation(self) -> List[int]:
        ...
    
    def sortDictByValue(self, d) -> Dict[int, int]:
        return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
            
    def Enviroment(self):
        evList = self.Evaluation()
        for _ in range(self.EVALUATEDELETESIZE):
            self.population.evaluationDeath(evList.pop(0))
        self.population.randomDeath(self.RANDOMDELETESIZE)
    
    
    
    def startFunc(self):
        ...
        
    def endFunc(self):
        self.DataSampling.pop()
        
    def loopFunc(self):
        for ind in self.population.Individuals:
            self.DataSampling[self.DataSamplingIndex].append(self.phenotype(ind.GeneCode))
        self.DataSamplingIndex += 1
        self.DataSampling.append([])
    
    def phenotype(self, gene):
        ...
        