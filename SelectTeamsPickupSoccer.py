import math
import os
import random

clean_screen = os.system('cls' if os.name == 'nt' else 'clear')

print ('-'*70)
print ('-'*70)
print ('               **LET\'S MOUNT TEAMS FOR PICK-UP GAME!**')
print ('-'*70)
print ('-'*70)
input('press any key for start...')

clean_screen = os.system('cls' if os.name == 'nt' else 'clear')

while True: # separate gold players and normal players
    try:
        print ('-'*120)
        count_all_players = 2*(int(input('          How many players on each team? (between 2 and 7)? ')))
        os.system('cls' if os.name == 'nt' else 'clear')

        if count_all_players > 3 and count_all_players < 15:
            print ('-'*120)
            print ('                                  ** Starting formation {} x {}! **'.format((int(count_all_players/2)),(int((count_all_players/2)))))         
            break
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print ('Value must be a number between 2 and 7')

    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('Value must be a number between 2 and 7')

print ('-'*120)
print ('''      
#                                         **GOLD PLAYERS**
#
#           GOLD PLAYERS are players that must be separated between teams to generate balance!
#                               NORMAL PLAYERS are just the normal players..
#                                      
#                          in the end, the program will to draw the teams!
#
#         ''')
print ('-'*120)


gold_players = []
left_players = []
count_gold_players=0
count_left_players=0
i=1
while True: 
    try:   
        while i <= count_all_players:
            print ('-'*120)
            player = str(input("Enter the name of the {}st player: ".format(i)))
            print ('-'*120)
            if player != '':
                type_player = int(input('Is {} a GOLD player or is just a NORMAL player? GOLD(1) or NORMAL(2): '.format(player)))
                print ('-'*120)
                if type_player == 1:
                        gold_players.append(player)
                        print('GOLD PLAYERS:',gold_players,'NORMAL PLAYERS',left_players)
                        count_gold_players+=1
                        i+=1 
                elif type_player == 2:
                        left_players.append(player)
                        print('GOLDER PLAYERS:',gold_players,'NORMAL PLAYERS',left_players)
                        count_left_players+=1
                        i+=1 
                else:
                    print('type 1 for GOLD or 2 for NORMAL ')
            else:
                print('player cannot be empty!')
        else:
            break                 
    except:
        print('type 1 for GOLD or 2 for NORMAL!')



if count_left_players == 0: # if there are only GOLD PLAYERS

    random.shuffle(gold_players)
    team_1 = []
    team_2 = []
    for j in range(count_gold_players):
        if (j%2) == 0 or j==0:
            team_1.append(gold_players[j])
        else:
            team_2.append(gold_players[j])
        j+=1

elif count_left_players == count_all_players: # if there are only NORMAL PLAYERS
    
      
    random.shuffle(left_players)
    team_1 = []
    team_2 = []
    for h in range(count_left_players):
        if (h%2) == 0 or h==0:
            team_1.append(left_players[h])
        else:
            team_2.append(left_players[h])
        h+=1
    
else: # if there are GOLD and NORMAL players


    random.shuffle(gold_players)
    random.shuffle(left_players)
    team_1 = []
    team_2 = []

    for j in range(count_gold_players):

        if (j%2) == 0 or j==0:
            team_1.append(gold_players[j])
        else:
            team_2.append(gold_players[j])
        j+=1


    for h in range(count_left_players):
        
        if len(team_1) < int(count_all_players/2):
            team_1.append(left_players[h])
        else:
            team_2.append(left_players[h])
        h+=1


print ('-'*120)
print ('#            TEAMS')
print ('#  TEAM A  :',team_1)
print ('#  TEAM B  :',team_2)


    





    













                 
            
            