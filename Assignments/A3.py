import random


def ascii_name_plaque(name):
    '''
    (str)->None
    Draws/Prints name plaque
    '''

    print()
    print(5*"*" + len(name)*"*" + 5*"*")
    print("*" + 4*" " + len(name)*" " + 4*" " + "*")
    print("*  " + 2*"_" + name + 2*"_" + "  *")
    print("*" + 4*" " + len(name)*" " + 4*" " + "*")
    print(5*"*" + len(name)*"*" + 5*"*")
    print()

    
def shuffle_deck(deck):
    '''
    (list of str)->None
    Shuffles the given list of strings representing the playing deck    
    '''
    
    print("Shuffling the deck...\n")
    random.shuffle(deck)

    
def create_board(size):
    '''
    int->list of str
    Precondition: size is even positive integer between 2 and 52
    Returns a rigorous deck of cards for you
    '''

    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i] = letter
          board[i+ len(board)//2] = board[i]
          letter = chr(ord(letter)+1)

    return board

def print_board(a):
    '''
    (list of str)->None
    Prints the current board in a nicely formated way
    '''

    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    
    print()
    
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''
    ()->None
    Pauses the program/game until the player presses enter
    '''
    
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''
    (list of str, int, int, list of str) -> None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''

    discovered[p1 - 1] = original_board[p1 - 1]  # Note: This alters the "discovered" list
    discovered[p2 - 1] = original_board[p2 - 1]
    
    print_board(discovered)
    print()
    

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################


def read_raw_board(file):
    '''
    str -> list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''

    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i] = raw_board[i].strip()

    return raw_board


# This functions does at most O(n log n) operations where n = len(l)
# If input list l was already sorted then l=sorted(l) line could be removed and
# the resulting funciton would do at most O(n) operations where n = len(l)
#
def clean_up_board(l):
    '''
    list of str -> list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''

    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board = []

    l = sorted(l) # O(n log n)
    #print(l)
    i = 0
    while i<len(l)-1: # O(n)
        card1 = l[i]
        card2 = l[i+1]
        if card1==card2 and card1!='*': #discovered pair of same cards
            playable_board.append(card1)
            playable_board.append(card2)
            i=i+1           

        # else do not copy this one. It is the odd card
        i=i+1

    return playable_board

# This functions does at most O(n log n) operations where n = len(l)
# If input list l was already sorted then l=sorted(l) line could be removed and
# the resulting funciton would do at most O(n) operations where n = len(l)
#
def is_rigorous(l):
    '''
    list of str -> bool or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    if not l: return True
    
    l.sort() # O(n log n)
    for i in range(len(l)-2): # O(n)
        if l[i]==l[i+2]: # l[i] appearst at least 3 times in the list
            return False

    return True
                
        

####################################################################3

def play_game(board):
    '''
    (list of str) -> None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")
    # The following line of code creates a list indicating what locations are paired, i.e., discovered
    # At the begining none are, so default initializaiton to False is ok
    # You may find this useful

    discovered = ["*"]*len(board)
    
    guesses = 0
    
    while discovered != board:
        print_board(discovered)
        
        print("\n")
        
        p1 = 0
        p2 = 0
        
        while p1 == p2 or p1 not in range(1, len(board) + 1) or p2 not in range(1, len(board) + 1) or discovered[p1-1]!='*' or discovered[p2-1]!='*':
            print("")
            print("Enter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, " + str(len(board)) + "]")
            p1 = int(input("Enter position 1: "))
            p2 = int(input("Enter position 2: "))
            flag = True # assume both positions good
            if p1 not in range(1, len(board) + 1) or p2 not in range(1, len(board) + 1):
                print("One of both of your chosen positions is out of range.")
                flag = False # one or both positions are bad
            else:
                if discovered[p1-1]!='*' or discovered[p2-1]!='*':
                    print("One or both of your chosen positions has already been paired.")
                    flag = False # one or both positions are bad
                if p1 == p2:
                    print("You chose the same positions.") 
                    flag = False # one or both positions are bad
            if not flag: # if positions are bad type a 
                print("Please try again. This guess did not count. You current number of guesses is ", str(guesses)+".")

        print_revealed(discovered, p1, p2, board)
        wait_for_player()
        print("\n"*50)


        if discovered[p1-1] != discovered[p2-1]:   # Note: This removes the revealed positions if they don't match 
            discovered[p1-1] = "*"
            discovered[p2-1] = "*"

        guesses += 1
    
    print("Congratulations! You completed the game with " + str(guesses) + " guesses. That is " + str(guesses - len(board)//2) + " more than the best possible.")



   # YOUR CODE GOES HERE
   # this is the funciton that plays the game



# MAIN
if __name__ == "__main__":
    ascii_name_plaque("Welcome to my Concentration game")
    print()

    print("Would you like (enter 1 or 2 to indicate your choice):")
    print("(1) me to generate a rigorous deck of cards for you")
    print("(2) or, would you like me to read a deck from a file?")

    choice = int(input())
    while choice!=1 and choice!=2:
        print(choice, "is not existing option. Please try again. Enter 1 or 2 to indicate your choice")
        choice=int(input())

    if choice==1:
        print("You chose to have a rigorous deck generated for you")
        size = -1
        while size%2 or size not in range(0,53):
           size = int(input("\nHow many cards do you want to play with?\nEnter an even number between 0 and 52: "))

        # this creates the board for you of the given size
        board = create_board(size)

    else: # choice ==2
        print("You chose to load a deck of cards from a file")
        filename = input("Enter the name of the file: ")
        filename = filename.strip()
        board = read_raw_board(filename)
        board = clean_up_board(board)
        if is_rigorous(board):
            s = "This deck is now playable and rigorous and it has {} cards.".format(len(board))
            ascii_name_plaque(s)

        else:
            s = "This deck is now playable but not rigorous and it has "+str(len(board))+" cards."
            ascii_name_plaque(s)

        wait_for_player()
        print("\n"*50)

            
    shuffle_deck(board)
    wait_for_player()
    print("\n"*50)
    if not board:
        print("\nThe resulting board is empty. \nPlaying Concentration game with an empty board is impossible.\nGood bye")
    else:
        play_game(board)
