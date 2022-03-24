import random
cost = 0.5
base_cost = cost
efficiency = 1

def gen_new_cost(allowance):
    global cost
    cost = allowance * ((2 * cost) - (base_cost/(1+random.randrange(5))))
    return cost

def get_num_plants(allowance):
    return((1 + random.random()*allowance/50))

def cpu_purchase(money):
    return money/cost