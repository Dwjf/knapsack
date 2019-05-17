import random

value = [
    44090,49643,248559,23209,307481,
    3936,87956,106463,143994,312835,
    149083,182022,328930,144721,64607
     ]
cost = [
    27992,10992,48600,16691,24688,
    11400,25164,27992,35220,39920,
    31424,21560,66420,33800,26500
]

constraint = 200000

def generate_chrome(num_gene=15):
    '''generate one random chromosome values '''
    chromosome = []
    for i in range(num_gene):
        gene=random.randint(0,1)
        chromosome.append(gene)
    return chromosome

def score_weight(chromosome,cost):
    '''to score one chromosome

    chromosome: list
    '''
    weightlist=[]
    for i in range(len(chromosome)):
        score=cost[i]*chromosome[i]
        weightlist.append(score)
    return sum(weightlist)

import datetime

startTime = datetime.datetime.now()

def display(guess):
        timeDiff = datetime.datetime.now() - startTime
        #fitness = get_fitness(guess)
        fitness = score_value(guess,value)
        weight = score_weight(guess,cost)
        print("{0}\t{1}\t{2}\t{3}".format(guess, fitness,weight, str(timeDiff)))


def score_value(chromosome,value):
    '''to score one chromosome

    chromosome: list
    '''
    valuelist=[]
    #print(chromosome)
    for i in range(len(chromosome)):
        score=value[i]*chromosome[i]
        valuelist.append(score)
    return sum(valuelist)

#print(generate_chrome())
def is_feasible(weightscore,constraint):
    if weightscore < constraint:
        return True
    return False


print(score_weight(generate_chrome(),cost))
'''
def execute():
    '''
'''generate and return feasible chromosome binary, weight, and
    value score, and assign value to max
    if is better score than previous
'''
'''
    current_binary=[]
    max_value = 0
    c = generate_chrome()
    print("c",c)
    w=score_weight(c,cost)
    print("Weight score",w)
    print("Constraint",constraint)
    v=score_value(c,value)
    print("Value score",v)
    if is_feasible(w,constraint):
        print("Feasible")
        current_binary = c
        max_value = v
        print(
        "Max chromosome",current_binary,
        "value is:",max_value
        )
    else:
        #return False
        print("Not Feasible solution")
     '''   
def iteration(n):
    "Iterate and save best result"
    optimal=0
    best_binary=[]
    for i in range(n):
       # print(i)
        c=generate_chrome()
        #print("Chromosome values",c)
        v = score_value(c,value)
        #print("V values:",v)
        w = score_weight(c,cost)
       # print("Weight values",w)
        if is_feasible(w,constraint):
            if v>optimal:
                optimal=v
                best_binary=c
                best_weight = w
                #print("Feasible Value",optimal,"at iteration",i,
                #"Optimal binary",best_binary,"Weight:",best_weight)
                display(best_binary)
    #return optimal,"Best binary is",best_binary,"at weight of:",best_weight
    #return display(best_binary)

iteration(40000)
#execute()
'''
c=generate_chrome()
score_value(c,value)

'''
