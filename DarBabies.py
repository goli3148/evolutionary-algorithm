from typing import List, Dict
from EA.EA import EA
from matplotlib import pyplot
from statistics import mean

class DarBabies(EA):
    GENESIZE = 8 # Length of Gene
    NUECLOETIDEDOMAIN = [0,1] # Domain of Nucleotides. forexample A,T,C,G in human
    
    POPULATIONSIZE = 16 # The number of individuals
    EVALUATEDELETESIZE = 4 # Number of Inidividual which will be deleted according to their score of evaluation
    RANDOMDELETESIZE = 4 # Number of Individual which will be deleted randomly by the environment
    POPULATIONCROSSOVERS = 8 # Number of Individual which will be generated by crossover using parents
    
    # Number of Mutation. if MUTATIONSIZE is bigger than the children of new generation,
    # every children will be mutated more than once, precisely equals to = MUTATIONSIZE / POPULATIONCROSSOVERS
    MUTATIONSIZE = 8
    
    # Number of loop to run EA algorithm.
    REPEATLOOP = 50
    
    def Evaluation(self) -> List[int]:
        # evaluateDict -> [ID:SCORE]
        # evaluation: more white: more score
        evaluateDict: Dict[int,int] = {}
        for ind in self.population.Individuals:
            evaluateDict[ind.ID] = self.phenotype(ind.GeneCode)
        evaluateDict = self.sortDictByValue(evaluateDict)
        return [key for key in evaluateDict.keys()]
    
    def phenotype(self, gene):
        decimal = 0
        for g in gene:
            decimal = decimal * 2 + g
        return decimal / 255

    def startFunc(self):
        print("DARBABIES PROJECT:")
        
    def endFunc(self):
        super().endFunc()
        meanColor = []
        x = []
        for time in range(len(self.DataSampling)):
            meanColor.append(mean(self.DataSampling[time]))
            x.append(time)
        pyplot.plot(x, meanColor)
        pyplot.show()
        
        for time in range(len(self.DataSampling)):
            temp = []
            for dataI in range(len(self.DataSampling[time])):
                temp.append(self.DataSampling[time][dataI])
                pyplot.scatter(dataI,dataI,color=str(temp[-1]))
            pyplot.show()
        
DarBabies().run()
