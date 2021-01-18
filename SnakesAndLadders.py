#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint


# In[2]:


def opening_msg():
    print("###### Welcome to Snakes & Ladders Game ######\n")


# In[3]:


def strt_msg():
    print("\n###### Let us Start ######\n")


# In[4]:


def get_playerNames():
    player1 = input("Enter the name of player 1:").strip()
    player2 = input("Enter the name of player 2:").strip()
    return player1,player2


# In[5]:


def autogameplay(player1,player2):
    players = (player1,player2)
    playername1 = player1 + ":"
    playername2 = player2 + ":"
    playernames = (playername1,playername2)         #names no change so use tuple
    playerscores = [0,0]                            #scores change so use list
    snakes = {17:7,54:34,62:19,98:79}
    ladders = {3:38,24:33,42:93,72:84}
    turn = None
    i = 0
    while turn != "quit":
        turn = input(playernames[i])
        if turn == "roll":
            curr = randint(1,6)
            print("You got a",curr)
        elif turn == "quit":
            print(players[1-i],"won the game")
            return 1
        else:
            print("Invalid Output")
            continue
        # calculating score upto point
        if playerscores[i] + curr <= 100:
            playerscores[i] = playerscores[i] + curr
            # encountering a ladder
            for l in ladders:
                if l == playerscores[i]:
                    playerscores[i] = ladders[l]
            #encountering a snake
            for s in snakes:
                if playerscores[i] == s:
                    playerscores[i] = snakes[s]
        print("Your final position is",playerscores[i])
        if playerscores[i] == 100:
            print(players[i],"won the game")
            return 1
        if playerscores[i] > 100:
            continue
        i=1-i                                              #change turn
    return 1
#autogameplay("Sanchal","Sambit")


# In[8]:


def manualgameplay(player1,player2):
    players = (player1,player2)
    playername1 = player1 + ":"
    playername2 = player2 + ":"
    playernames = (playername1,playername2)         #names no change so use tuple
    playerscores = [0,0]                            #scores change so use list
    snakes = {17:7,54:34,62:19,98:79}
    ladders = {3:38,24:33,42:93,72:84}
    turn = None
    i = 0
    while turn != "quit":
        turn = input(playernames[i])
        if turn.isdigit():
            curr = int(turn)
            if curr < 1 or curr > 20:                    # assume 1 and 20 both include
                print("Invalid Input")
                continue
        else:
            if turn == "quit":
                print("\n",players[1-i],"won the game")
                return 1
            else:
                print("Invalid Input")
                continue
        
        print("You got a",curr)
        
        # calculating score upto point
        if playerscores[i] + curr <= 100:
            playerscores[i] = playerscores[i] + curr
            # encountering a ladder
            for l in ladders:
                if l == playerscores[i]:
                    playerscores[i] = ladders[l]
            #encountering a snake
            for s in snakes:
                if playerscores[i] == s:
                    playerscores[i] = snakes[s]
            
        print("Your final position is",playerscores[i])
        if playerscores[i] > 100:
            continue
        if playerscores[i] == 100:
            print("\n",players[i],"won the game")
            return 1
        i=1-i                                                 #changing turn
    return 1
#manualgameplay("Sanchal","Sambit")


# In[6]:


def begin():
    opening_msg()
    player1_name,player2_name = get_playerNames()
    strt_msg()
    mode = input("Enter the mode:")
    # separate the modes 
    if mode == "Auto":
        print("\n*****Game started in Auto mode*****\n")
        ans = autogameplay(player1_name,player2_name)
    elif mode == "Manual":
        print("\n*****Game started in Manual mode*****\n")
        ans = manualgameplay(player1_name,player2_name)
    else:
        print("Invalid Input")
    if ans == 1:
        print("\n##### Game Successfully finished #####")
    return


# In[9]:


if __name__ == "__main__":
    begin()


# In[ ]:


#Name: Sanchal Bhattacharya
#Rollno: 1805155
#House: Gollum

