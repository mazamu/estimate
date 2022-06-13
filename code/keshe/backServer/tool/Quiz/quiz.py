import csv
import random
import pandas as pd
class quiz():
    def __init__(self):
        ## 雅思词汇答对个数
        self.ieltsCounter = 0
        ## 四六级词汇答对个数
        self.cetCounter = 0
        ## 考研词汇答对个数
        self.bstsCounter = 0

        ## 雅思权重
        self.weightIelts = 0.6
        ## 四六级权重
        self.weightcet = 0.25
        ## 考研权重
        self.weightBsts = 0.15
        self.path = "/Estimation-vocabulary/code/keshe/backServer/tool/Quiz/"
        
    ## 读取每个词库的csv文件
    def GetWordcsv(self):
        # 读取雅思词汇
        wordList1 = pd.read_csv(self.path + 'ielts1.csv')['word'].tolist()
        # 读取四六级词汇
        wordList2 = pd.read_csv(self.path + 'cet1.csv')['word'].tolist()
        # 读取考研词汇
        wordList3 = pd.read_csv(self.path + 'bsts1.csv')['word'].tolist() 
        for i in range(len(wordList1) - 1, -1, -1):
            if wordList1[i] in wordList2:
                del wordList1[i]
                
        for i in range(len(wordList3) - 1, -1, -1):
            if wordList3[i] in wordList2:
                del wordList3[i]
                
        return wordList1,wordList2,wordList3

    def Problem(self, wordList1, wordList2, wordList3,problemNum=100):
        ## 出题
        problem = [{'word':None,'flag':False} for i in range(problemNum)]
        
        ## 每一个题库抽题数
        self.ieltsNum = int(problemNum*self.weightIelts)
        self.cetsNum = int(problemNum*self.weightcet)
        self.bstsNum = int(problemNum*self.weightBsts)
        problemList = []
        
        self.ieltsNum = int(problemNum * (len(wordList1)/(len(wordList1) + len(wordList2) + len(wordList3))))
        ieltsList = random.sample(wordList1, self.ieltsNum)
        problemList = problemList + ieltsList
        
        self.cetsNum = int(problemNum * (len(wordList2)/(len(wordList1) + len(wordList2) + len(wordList3))))
        cetsList = random.sample(wordList2, self.cetsNum)
        problemList = problemList + cetsList
        
        self.bstsNum = problemNum - self.ieltsNum - self.cetsNum
        bstsList = random.sample(wordList3, self.bstsNum)
        problemList = problemList + bstsList
                       
        random.shuffle(problemList)
        for i in range(len(problemList)):
            problem[i]['word'] = problemList[i]
        return problem


    ## 统计答卷情况
    def getResult(self,answer,wordList1,wordList2,wordList3):
        ieltsrightCount = 0
        cetrightCount = 0
        bstrightCount = 0
        
        for i in range(len(answer)):
            strTemp = str(answer[i]['word'])
            if answer[i]['flag'] == True and strTemp in wordList1:
                ieltsrightCount += 1
            elif answer[i]['flag'] == True and strTemp in wordList2:
                cetrightCount += 1
            elif answer[i]['flag'] == True and strTemp in wordList3:
                bstrightCount += 1
            else:
                continue
        return ieltsrightCount, cetrightCount, bstrightCount

    ## 分析答卷结果（预估词汇量）
    def evaluateResult(self,result,wordList1,wordList2,wordList3):
        ieltsrightCount, cetrightCount, bstrightCount = result
        ieltRightRate = ieltsrightCount / self.ieltsNum
#         print(ieltsrightCount)
        cetRightRate = cetrightCount / self.cetsNum
#         print(cetrightCount)
        bstRightRate = bstrightCount / self.bstsNum
#         print(bstrightCount)
        totalRate = 0
        totalRate = ieltRightRate * self.weightIelts + cetRightRate * self.weightcet \
        + bstRightRate * self.weightBsts
        total = int((len(wordList1) + len(wordList2) + len(wordList3)) * totalRate)
#         print(len(wordList1) + len(wordList2) + len(wordList3))
        return total
    
    

