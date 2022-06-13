import pandas as pd
import random
import csv

if __name__ == '__main__':
    w0 = []
    with open("./ielts.csv","r")
        reader = csv.reader(csvfile)
        for line in reader:
            w0 = w0 + line
    
    w1 = []
    with open("./cet.csv","r")
        reader = csv.reader(csvfile)
        for line in reader:
            w1 = w1 + line
            
    w2 = []
    with open("./bst.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            w2 = w2 + line

    for i in range(len(w0) - 1, -1, -1):
        if w0[i] in w1:
            del w0[i]

    for i in range(len(w2) - 1, -1, -1):
        if w2[i] in w0:
            del w2[i]

    print('ielt={}\t \ncounts={}'.format(w0, len(w0)))
    print('cet={}\t \ncounts={}'.format(w1, len(w1)))
    print('bst={}\t \ncounts={}'.format(w2, len(w2)))

    ## Problem Setting ## 5701words
    problem = []
    ## first Level
    ielts = random.sample(w0, 30)
    problem = problem + ielts
    # print('ielt={}\t \ncounts={}'.format(problem, len(problem)))
    ## second level
    cets = random.sample(w1, 40)
    problem = problem + cets

    # print('ielt={}\t \ncounts={}'.format(problem, len(problem)))

    ## third level
    bsts = random.sample(w2, 30)
    problem = problem + bsts

    random.shuffle(problem)
    ## test
    ans = []
    for i in range(len(problem)):
        ans.append(random.choice([True, False]))
        # ans.append(True)

    ## evaluate
    ieltsCounter = 0
    cetCounter = 0
    bstsCounter = 0
    for i in range(len(problem)):
        if ans[i] == True:
            if problem[i] in ielts:
                ieltsCounter += 1
            elif problem[i] in cets:
                cetCounter += 1
            else:
                bstsCounter += 1

    print(ieltsCounter)
    print(cetCounter)
    print(bstsCounter)
    rate = 0
    weightIelts = 0.3
    weightcet = 0.4
    weightBsts = 0.3

    # ielts
    rate += ((ieltsCounter/len(ielts)) * weightIelts)
    # cet
    rate += ((cetCounter/len(cets)) * weightcet)
    # bst
    rate += ((bstsCounter/len(bsts)) * weightBsts)
    print('total=', int((len(w0)+len(w1)+len(w2))*rate))