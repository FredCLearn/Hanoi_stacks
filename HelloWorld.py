#gamecode

from stack import *

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack,middle_stack,right_stack]


#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks,0,-1):
    left_stack.push(disk)

num_optimal_moves = (2** num_disks) - 1
print("\nThe fastest you can solve this game is in {0}".format(num_optimal_moves))

#Get User Input

def get_input():
    #get first letter for each stack in stack list
    choices = [stack.get_name()[0] for stack in stacks]

    while True:

        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("enter {0} for {1}".format(letter,name))

        #print(len(choices))

        user_input = input("")

        #validating user input
        if user_input in choices:
            #print(len(choices))
            #print(choices)
            #print(choices.index(user_input))
            for i in range(len(stacks)):
                #print("you entered one of the choices")
                #print(stacks[1].get_size())
                #print(stacks[1].print_items())
                #print("stack number")
                #print(i)
                return stacks[choices.index(user_input)]
        else:
            print("you did not enter one of the correct choices")



#Play the Game

num_user_moves = 0

#game ends when all disks are on the right most stack
while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")

    for stack in stacks:
        stack.print_items()
        print(stack.get_size())

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        #debug
        print("this is the from stack - " + str(from_stack.get_size()))
        print(to_stack.get_size())

        #check bad inputs (moving from empty stack, move a larger disk onto a smaller disk)
        if from_stack.get_size() == 0:
            print("\n\nInvalid Move. Try Again1")
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves +=1
            break
        else:
            print("\n\nInvalid Move. Try Again23")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
