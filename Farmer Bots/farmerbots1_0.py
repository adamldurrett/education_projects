import random
import time
# globals
round_num = 1
final_round = 5
playing = True
score = 0

bots = ['Planter', 'Raiser', 'Harvester']
efficiencies = [1, 5, 10]
prices = [0]*len(bots)
price_scale = [1,10,100]

jobs = ['Plant Seeds', 'Water Crops', 'Harvest Crops']
job_counts = [0]*len(bots)
job_scale =[100,10,1]

allowance = 0
player_picks = [1]*len(bots)
cpu_picks = [1]*len(bots)

# functions
def setup_round():
    global allowance
    global prices
    global job_counts
    global player_picks
    global cpu_picks

    for i in range(3):
        prices[i] = price_scale[i] * (random.randrange(5) + 1) * round_num
        job_counts[i] = job_scale[i] * (random.randrange(100) + 50) * round_num
        
    allowance = round_num * 500 + max(prices) * 10
    player_picks = [1]*len(bots)
    cpu_picks = [1]*len(bots)


# shows the amount of tasks needed to be completed for each job
def display_tasks():
    print(" This Round's Tasks:")
    for i in range(3):
        print(str(i) + ". " + jobs[i] + " : " + str(job_counts[i]) + " times.")
    print()

# shows all the available robot options
def display_shop():
    # 28 chars: 16 + 12 chars used from start to last " " before efcy.
    print("Robots in stock:" + " "*12 + "efcy.  cost  Qty   total price")

    for i in range(3):
        # 28 - (1 + 1 + len(bots[i]) + 5)
        print(str(i) + ". " + bots[i] + " Bots" + " "*(21-len(bots[i])) + str(efficiencies[i]) + "/s    $" + str(prices[i]) + "     " + str(player_picks[i]) + "     $" + str(player_picks[i]*prices[i])) 
    print()


# Asks the player for what they would like to purchase
def get_player_input():
    global player_picks
    
    i = 0
    while i < 3:
        display_tasks()
        display_shop()
        total_cost = 0
        for x in range(3):
            total_cost += prices[x] * player_picks[x]
        print("  This Round's Allowance: $" + str(allowance) + "     $" + str(allowance-total_cost) + " remaining.")
        valid_input = False

        print("How many " + bots[i] + " Bots would you like to purchase?")
    
        while(not valid_input):
            choice = input()
            if(choice.isnumeric()):
                choice = int(choice)
                if(choice<1):
                    print("Please, choose a value greater than 0.")
                
                player_picks[i] = choice
                total_cost = 0
                for z in range(3):
                    total_cost += player_picks[z] * prices[z]
                
                if(total_cost>allowance):
                    print("Exceeds maximum allowance by " + str(total_cost-allowance) + "!")
                    print("Please choose a lower value.")
                else:
                    valid_input = True
                    i += 1
            else:
                if(choice == "undo"):
                    if(i>0):
                        i -= 1
                        player_picks[i] = 1
                        valid_input = True
                        print()
                    else:
                        print("No more to undo. \n")
                else:
                    print("Please, enter a valid number.")
        

# randomly decides what the cpu chooses                
def get_cpu_input():
    global cpu_picks
    weights = [1,1,1]
    min_weight = int(100*max(prices)/allowance) + 1

    for i in range(3):
        weights[i] = random.randrange(100)
    total_weight = sum(weights)
    for i in range(3):
        weights[i] = weights[i]/total_weight

    for i in range(3):
        cpu_picks[i] = int(weights[i] * allowance / prices[i]) + 1


def determine_winner():
    global score
    cpu_times = [0,0,0]
    player_times = [0,0,0]

    for i in range(3):
        cpu_times[i] = job_counts[i] / (cpu_picks[i] * efficiencies[i])
        player_times[i] = job_counts[i] / (player_picks[i] * efficiencies[i])

    player_timing = max(player_times)
    cpu_timing = max(cpu_times)

    time.sleep(1)
    print("\n Player time: " + str(player_timing))
    time.sleep(3)
    print(" CPU time: " + str(cpu_timing) + "\n")
    time.sleep(2)
    if(player_timing<=cpu_timing):
        print(" You win Round " + str(round_num))
        score = score + 1
    else:
        print(" You lose Round " + str(round_num))
    time.sleep(4)
    print("\n\n")


# main loop
while(playing):

    if(round_num == final_round):
        playing = False
    
    print("\n\n\n-----= Round ", round_num, " =-----")
    setup_round()

    get_player_input()
    get_cpu_input()

    determine_winner()

    round_num += 1

print("Your score was: " + str(score) + " out of " + str(final_round) + " rounds.")
