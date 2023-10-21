from .Gene import Gene
from typing import List, Any

class Individual(Gene):
    Parenting: bool
    ID: int = 0
    def __init__(self, geneSize:int, nucleotideDomain:List[Gene.Nucleotide], id, gene=None, randomCreation=True) -> None:
        super().__init__()
        self.Parenting = False
        self.ID = id
        self.GeneSize = geneSize
        self.NucleotideDomain = nucleotideDomain
        if randomCreation: self.createRandomIndividual()
        else: self.createIndividual(gene=gene)
        
    def createRandomIndividual(self)->None:
        self.createRandomGene()
        
    def createIndividual(self, gene)->None:
        self.createGene(gene=gene)
        
    def genotype(self) -> Gene.GeneCode:
        return self.GeneCode
    
    def phenotype(self) -> Any:
        ...
