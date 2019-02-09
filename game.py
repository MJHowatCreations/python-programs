import random

class Player:
    position = 0
    money = 1500
    def __init__(self, name):
        self.name = name

class Property:
    owned = False
    def __init__ (self, name, value, group_amount):
        self.name = name # Name of property when landed on
        self.value = value # Value of property to buy
        self.group_amount = group_amount #Number of properties to make a set


def starting_game(): # Needs to be able to take inputs other then "Yes" / "1-4"
    playing = raw_input("Do you wish to play? ")
    if playing == "Yes" or len(playing) > 1:
        players = int(raw_input("How many players will there be? (1-4): "))
        return players
    else:
        print "Thanks for playing!"
        quit()
        
def rolling_dice(previous_total_roll, roll_again, number_of_rolls): #Need to create a way to check for doubles, triples , go to jail    
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    total_roll = die_1 + die_2
    while number_of_rolls < 3:
        if die_1 == die_2:
            print "Lucky! You rolled double", str(die_1) + "'s. You will move", total_roll, "spaces and can roll again!"
            number_of_rolls += 1
            roll_again = True
            return total_roll, roll_again, number_of_rolls
        else:    
            print "You rolled a", str(die_1), "and a", str(die_2) + "."
            print "You will move", total_roll, "spaces."
            number_of_rolls += 1
            roll_again = False
            return total_roll, roll_again, number_of_rolls
    else:
        print "Go to jail!"
        total_roll = 0
        roll_again = False
        number_of_rolls += 1
        return total_roll, roll_again, number_of_rolls
    
def moving_spaces(dice_roll, original_position):
    new_position_before_go = dice_roll + original_position
    if new_position_before_go >= 40:
        final_position = (new_position_before_go - 40)
        return final_position, True
    else:
        return new_position_before_go, False
        
    
def go_rules(money): #Test function to see a if money works needs to change into a more useful function
        print "You passed GO! Here is 200 dollars. You now have", (money + 200),
        print "dollars"
        return 200

#def landing on a spot
#def checking if spot is owned
#def buying spot
#def auctioning spot
#def checking spot ownership
#def paying rent
#def player cant pay rent
#def mortaging property
#def selling property
#def subtracting rent
#def adding rent
#buying houses
#def trading
#def chance / community chest spaces

player_list = []
is_playing = starting_game()
while is_playing > 0: #Creates a list of Player_objects to assign position and money to. I need to debug non integer / 0 answers. Works correctly with ideal responses
    if is_playing == 4:
        player_4 = Player("Player 4")
        player_list.append(player_4)
        is_playing -= 1
    elif is_playing == 3:
        player_3 = Player("Player 3")
        player_list.append(player_3)
        is_playing -= 1
    elif is_playing == 2:
        player_2 = Player("Player 2")
        player_list.append(player_2)
        is_playing -= 1
    elif is_playing == 1:
        player_1 = Player("Player 1")
        player_list.append(player_1)
        is_playing -= 1
        game_start = True
        player_list.reverse()
    else:
        print "That input is unsupported, please enter a new number "
        is_playing = starting_game()
        

while game_start == True:
    for players in player_list:
        dice_data = [0, None, 0]
        print "It is", players.name + "'s turn to roll the dice!"
        dice_data = rolling_dice(dice_data[0], dice_data[1], dice_data[2])
        moving_data = moving_spaces(dice_data[0], players.position)
        players.position = moving_data[0]
        if moving_data[1] == True:
            players.money += go_rules(players.money)
        print "You are at the", players.position, "spot."
        
        while dice_data[1] == True: #double rules maybe pass in 
            dice_data = rolling_dice(dice_data[0], dice_data[1], dice_data[2])
            moving_data = moving_spaces(dice_data[0], players.position)
            players.position = moving_data[0]
            if moving_data[1] == True:
                players.money += go_rules(players.money)
            if dice_data[2] == 4:
                players.position = 10
            print "You are at the", players.position, "spot."
            
        print "------------------------------------"
    roll_again = raw_input("Do you want to roll again? ")
    if roll_again == "Yes":
        continue
    else:
        break

        break


        
        #A players turn starts with Rolling Dice, Moving spaces if pass go pay the person for go, landing on the spot, checking if spot is owned, if spot is not owned buying / auctioning it
#if spot is owned checking owner, seeing if player has enough money, if not mortaging / selling items, subtracting rent, adding rent to owner, buying houses, trading then turn over     
    
