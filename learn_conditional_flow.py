# Short script to demo conditional flow (while, for and if)
 # This script will ask for a word and spell it out letter by letter.
#  If the user enters "quit", the script will exit.

#  This mimics the conditional flow structure introduced in snake_game_v2.py

prompt = "\nEnter a word and I will spell it (or 'quit' to exit): "

game_over = False
while not game_over:
    word = input(prompt)
    if word == 'quit':
        game_over = True
    print(f"The word is: {word}")
    print("Spelling it out:", end = ' ')
    for letter in word:
        print(letter.upper(), end='-')
        if letter == 'z':
            print("** 10 points  **", end='')
        if letter == 'a':
            print("** 5 points  **", end='')
    
print("\nGoodbye!")