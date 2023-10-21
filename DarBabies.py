from typing import List, Dict
from EA.EA import EA
from matplotlib import pyplot
from statistics import mean

class DarBabies(EA):
    GENESIZE = 8
    NUECLOETIDEDOMAIN = [0,1]
    
    POPULATIONSIZE = 16
    EVALUATEDELETESIZE = 4
    RANDOMDELETESIZE = 4
    POPULATIONCROSSOVERS = 8
    
    MUTATIONSIZE = 16
    
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
