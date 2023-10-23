import random

print('Rules of the game: Rock Paper Scissors : \n')
"Rock vs Paper -> Paper wins \n"
"Rock vs Scissors -> Rock wins \n"
"Paper vs Scissors -> Scissor wins \n"

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice:"))


    while choice > 3  or choice < 1:
      choice = int(input('Enter a valid choice please :)'))


    if choice == 1:
      choice_name = 'Rock'
    elif choice == 2:
      choice_name = 'Paper'
    else:
      choice_name = 'Scissors'

    print('User choice is \n', choice_name)
    print('Computer Turn now...')


    comp_choice = random.randint(1,3)

    while comp_choice == choice:
      comp_choice = random.randint(1,3)

    if comp_choice == 1:
      comp_choice = 'ROCK'
    elif comp_choice == 2:
      comp_choice == 'PAPER'
    else:
      comp_choice == 'SCISSOR'

    print("Computer choice is \n", comp_choice)
    print(choice_name, 'VS', comp_choice)

    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"

    if (choice == 1 and comp_choice == 2):
        print('paper wins =>\n', end = "")
        result = 'PAPER'

    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>\n', end = "")
        result = 'PAPER'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end = "")
        result = 'ROCK'

    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end = "")
        result = 'ROCK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>\n', end = "")
        result = 'SCISSORS'

    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>\n', end = "")
        result = 'SCISSORS'

    if result == 'DRAW':
      print("<== It's a tie! ==>")

    if result == choice_name:
      print("<== User Wins! ==>")

    else:
      print("<== Computer Wins! ==>")

    print("Let's play again? (Y/N)")

    ans = input() .lower
    if ans == 'n':
        break


print("Thanks for playing!")