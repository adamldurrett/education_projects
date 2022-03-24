from secrets import choice
import planter
import raiser
import harvester
import random

def end_game():
    print("Game Over")

def calculate_times(pick_list, num_plants_list):
    timing_list = [0,0,0]
    timing_list[0] = num_plants_list[0] / (pick_list[0] * planter.efficiency)
    timing_list[1] = num_plants_list[1] / (pick_list[1] * raiser.efficiency)
    timing_list[2] = num_plants_list[0] / (pick_list[2] * harvester.efficiency)

    return timing_list
    

def play_round(round_level : int):
    allowance = 50 * round_level

    planter.gen_new_cost(allowance)
    raiser.gen_new_cost(allowance)
    harvester.gen_new_cost(allowance)

    bots = ['Planter', 'Raiser', 'Harvester']
    
    # determines the number of each plant that is getting harvested this round
    num_plants = [planter.get_num_plants(allowance),
                raiser.get_num_plants(allowance),
                harvester.get_num_plants(allowance)]

    print("\n\n+  Round ", round_level, " +")
    print("Prices:")
    print("    Planter: $", planter.cost, "  1 plant per second")
    print("    Raiser: $", raiser.cost, "   5 plants per second")
    print("    Harvester: $", harvester.cost, "   10 plants per second")

    current_selection = 0 # 0 for planter, 1 for raiser, 2 for harvester
    choices = [1,1,1] # [planters bought, raisers bought, harvesters bought]
    total_cost = 0 # used to keep track of money spent
    
    # Gathering player's inputs
    while(True):

        # have chosen amounts for each bot type
        if(current_selection >= len(choices)):
            if(input("Are you satisfied with your choices?") in ['yes','Yes','y','Y','ya']):
                break # locked in
            else:
                current_selection -= 1
            
    
        # still deciding
        valid_choice = False
        total_cost = choices[0] * planter.cost + choices[1] * raiser.cost + choices[2] * harvester.cost
        while(not valid_choice):
            choice = input("How many" + str(bots[current_selection]) + " Bots would you like to purchase?")

            # did the player choose a number?
            if(choice.isnumeric()):
                # recalculate total with new choice
                choices[current_selection] = int(choice)
                total_cost = choices[0] * planter.cost + choices[1] * raiser.cost + choices[2] * harvester.cost

                # new total exceeds round's allowance
                if(int(choice) < 1):
                    print("Cannot choose less than 1.")
                elif((total_cost > allowance)):
                    print("Error, $", total_cost - allowance, " more is needed")
                else:
                    # choice is accepted, and moves on to the next one
                    valid_choice = True
            # player choice isn't a number
            else:
                print("Please input a valid number.")
        
        current_selection += 1

    
    

    # determining percentages for computer
    planter_perc = random.randrange(91)
    raiser_perc = random.randrange(101-planter_perc)
    harvester_perc = 100 - planter_perc - raiser_perc

    # determining how much money it's spending on each
    planter_money = planter_perc * allowance
    raiser_money = raiser_perc * allowance
    harvester_money = harvester_perc * allowance


    # determining number of bots the computer purchased
    cpu_choices = [planter.cpu_purchase(planter_money), 
                    raiser.cpu_purchase(raiser_money), 
                    harvester.cpu_purchase(harvester_money)]

    cpu_timings = calculate_times(cpu_choices, num_plants)
    player_timings = calculate_times(choices, num_plants)

    if(max(cpu_timings) > max(player_timings)):
        print("cpu wins this round")
    else:
        print("you win this round")
        score += 1
        print("Score:", score)

def setup_game():
    global score
    global level
    score = 0
    rounds = 5
    print("rules")
    play = input("Do you want to play?")
    level = 1
    playing = True
    if(play in ['yes','Yes','y','Y','ya']):
        while(playing):
            if(level == rounds):
                playing = False
            play_round(level)
        
        end_game()
    else:
        print("Alright then. :(")
        end_game()


setup_game()