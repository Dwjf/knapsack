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
'''add constraint on cost value.'''

def generate_chrome(num_gene=15):
    '''generate one random chromosome values '''
    chromosome = []
    for i in range(num_gene):
        gene=random.randint(0,1)
        chromosome.append(gene)
    return chromosome

def score_weight(chromosome,cost):
    '''to score one chromosome.

    chromosome: list
    '''
    weightlist=[]
    for i in range(len(chromosome)):
        score=cost[i]*chromosome[i]
        weightlist.append(score)
    return sum(weightlist)

def score_value(chromosome,value):
    '''to score one chromosome

    chromosome: list
    '''
    valuelist=[]
    for i in range(len(chromosome)):
        score=value[i]*chromosome[i]
        valuelist.append(score)
    return sum(valuelist)

def is_feasible(weightscore,constraint):
    '''predicate on feasibility, that is values less than constraint'''
    if weightscore < constraint:
        return True
    return False
        
def main(n):
    "Iterate and save best result"
    optimal=0
    best_binary=[]
    for i in range(n):
        c=generate_chrome()
        v = score_value(c,value)
        w = score_weight(c,cost)
        if is_feasible(w,constraint):
            if v>optimal:
                optimal=v
                best_binary=c
                best_weight = w
                print("Feasible Value",optimal,"at iteration",i,
                "Optimal binary",best_binary,"Weight:",best_weight)
    return optimal,"Best binary is",best_binary,"at weight of:",best_weight

print("Optimal value of:",main(30000))

