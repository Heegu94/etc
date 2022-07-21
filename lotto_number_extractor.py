import numpy as np
from itertools import *
import random

class LottoNumExractor:
    def __init__(self,
                num_of_pick = [1 for a in range(45)],
                ):
    
        self.num_of_pick = num_of_pick
        self.percentages = self.each_percentages()
        self.splited_percentages = self.split_percentages()
        
    def each_percentages(self, ):
        sum_of_list = sum(self.num_of_pick)
        percentages=[n/sum_of_list for n in self.num_of_pick]
        return percentages

    def split_percentages(self, ):
        splited_percentages = [self.percentages[(10*idx):(10*idx)+split] for idx, split in enumerate([10,10,10,10,5])]
        return splited_percentages

    # METHOD 
    ## 같은 색에서 3개이상 나오지않게 6개 숫자 추출 + r각 숫자간 확률 적용.
    def ExtractionMethod(self, ):
        lotto = np.array([np.arange(1, 11), np.arange(11, 21), np.arange(21, 31), np.arange(31, 41), np.arange(41, 46)])
        combi = [0,0,0,1,1,1,1,1,1,2,2]
        combination = list(permutations(combi, 5))
        combi_list= []
        for nums in combination:
            if sum(nums) == 6:
                combi_list.append(nums)

        eachnums = random.choice(combi_list)
        lotto_paper = []
        idx = 0
        for n, percent in zip(eachnums, self.splited_percentages):
            mul_factor =(1.0/sum(percent))
            mul_percent = [pe*mul_factor for pe in percent]
            pickednums = np.random.choice(lotto[idx], size=n, replace=False, p=mul_percent)
            if len(pickednums)>1:
                for k in pickednums:
                    lotto_paper.append(k)
            elif len(pickednums)==0:pass
            else:
                lotto_paper.append(pickednums[0])
            idx +=1
        return sorted(lotto_paper)

    def __getnums__(self,):
        print(self.ExtractionMethod())
        print(self.ExtractionMethod())
        print(self.ExtractionMethod())
        print(self.ExtractionMethod())
        print(self.ExtractionMethod())

if __name__=="__main__":
    num_of_pick=[174,163,161,168,152,157,158,154,133,164,161,170,172,165,159,160,173,170,153,167,160,131,141,
                 163,150,164,174,144,142,151,160,142,169,177,156,156,163,163,168,163,142,157,180,158,160]

    lotto_num_extractor = LottoNumExractor(num_of_pick)
    lotto_num_extractor.__getnums__()
    