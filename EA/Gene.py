from typing import TypeVar, List, Dict
import random
import copy
sys_random = random.SystemRandom()

class Gene():
    Nucleotide = TypeVar("Nucleotide")
    NucleotideDomain: List[Nucleotide] = []
    
    GeneSize: int = 0
    GeneCode: List[Nucleotide] = []
    
    Mutaions: Dict[int, str] = {1:'Bit Flip', 2:'Bit Swap', 3:'Scramble', 4:"Inversion", 5: "None"}
    
    def __init__(self) -> None:
        self.GeneCode = []
        self.GeneSize = 0
        self.NucleotideDomain = []
    
    def createRandomGene(self) -> None:
        # if len(self.GeneCode) > 0: return
        for _ in range(self.GeneSize):
            nuc = random.choice(self.NucleotideDomain)
            self.GeneCode.append(nuc)
    
    def createGene(self, gene) -> None:
        self.GeneCode = gene
    
    def mutation(self, mutationType: int=None, randomSel=True) -> None:
        mutationType = random.choice(list(self.Mutaions.keys())) if randomSel else mutationType
        if mutationType == 1:
            BitFlipIndex = random.randint(0, self.GeneSize-1)
            BitFlipNucleotide = random.choice(self.NucleotideDomain)
            self.GeneCode[BitFlipIndex] = BitFlipNucleotide
        elif mutationType == 2:
            BitSwapIndex1 = random.randint(0, self.GeneSize-1)
            BitSwapIndex2 = random.randint(0, self.GeneSize-1)
            self.GeneCode[BitSwapIndex1], self.GeneCode[BitSwapIndex2] = \
                self.GeneCode[BitSwapIndex2], self.GeneCode[BitSwapIndex1]
        elif mutationType == 3:
            BitScramble1 = random.randint(0, self.GeneSize-1)
            BitScramble2 = random.randint(0, self.GeneSize-1)
            (BitScramble1, BitScramble2) = (BitScramble2, BitScramble1) \
                if BitScramble1 > BitScramble2 else (BitScramble1, BitScramble2)
            partialCopy = copy.deepcopy(self.GeneCode[BitScramble1:BitScramble2])
            random.shuffle(partialCopy)
            self.GeneCode[BitScramble1:BitScramble2] = partialCopy
            del(partialCopy)
        elif mutationType == 4:
            BitInversion1 = random.randint(0, self.GeneSize-1)
            BitInversion2 = random.randint(0, self.GeneSize-1)
            (BitInversion1, BitInversion2) = (BitInversion2, BitInversion1) \
                if BitInversion1 > BitInversion2 else (BitInversion1, BitInversion2)
            partialCopy = copy.deepcopy(self.GeneCode[BitInversion1: BitInversion2])[::-1]
            self.GeneCode[BitInversion1: BitInversion2] = partialCopy
            del(partialCopy)
        else:
            ...
