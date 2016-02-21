# This is my first attempt to play with dictonaries in python

import random
import os
import shelve

#   STOPPERS - keywords given by user to break the main loop and end the program
stoppers = ['quit', 'end', 'stop', 'die']

devCMDs = ['kill',]

basicCMDs = ['help', 'test1', 'test2']

dogLoot = ['5 Gold Coins']

npcs = {'dog': dogLoot}

inventory = {}

# TODO check if shelve data file is saved in CWD,
#       if not, call constructor

def killNPC(npcID):
    return npcs.get(npcID, 0)

def devTools(cmd):
    
    if cmd == 'kill':
        print(
'''You have selected the kill command. With this too you may kill any NPC by its npcID. 
Please enter the id now...'''
)
        npcID = raw_input('npcID: ')
        return killNPC(npcID)
    else:
        return

def printList(aList):
    string = ''
    for i in range(len(aList)):
        string = string + aList[i] + ', '
    return string

def basicCMD(cmd):
    if cmd == 'help':
        print('Developer Commands: ' + printList(devCMDs))
        print('Basic Commands: ' + printList(basicCMDs))

print('''The game is running, if at anytime you would like to quit please type any of the following: quit, end, stop, die.
You may also type help at anytime to veiw a list of commands.''')

while True:

    userInput = raw_input()
    userInput = userInput.lower()
    
    if userInput in stoppers:
        break
    elif userInput in devCMDs:
        print(devTools(userInput))
    elif userInput in basicCMDs:
        basicCMD(userInput)
    else:
        print(userInput)
