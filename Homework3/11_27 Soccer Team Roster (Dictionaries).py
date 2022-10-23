#Kaitlyn Sourignosack
#1824497

if __name__ == '__main__':
    count = 1
    playerdict = {}

    while count != 6:

        jerseynum = int(input (f'Enter player {count}\'s jersey number:'))
        print ()
        jersey = jerseynum

        playerrating = int(input(f'Enter player {count}\'s rating:'))
        print ()
        print ()
        playerrate = playerrating

        if jersey in range (0,100) and playerrate in range (1,10) and jersey not in playerdict.keys ():
            playerdict [jersey] = playerrate

        storinginitialdict = playerdict.copy()


        count += 1


    # outside while loop

    menu = str(input(''))


#PROGRAM

    if menu != 'q':

        # a input (add players)
        while menu != 'q':
            if menu == 'a':

                jerseynum = int(input('Enter a new player\'s jersey number:'))
                jersey = jerseynum

                playerrating = int(input('Enter a new rating for player:'))
                playerrate = playerrating

                if jersey in range(0, 99) and playerrate in range(1, 9) and jersey not in playerdict.keys():
                    playerdict[jersey] = playerrate

                menu = str (input('Choose an option:'))


            # o input (ROSTER)
            elif menu == 'o':
                print('ROSTER')
                for a, b in sorted(playerdict.items()):
                    print(f'Jersey number: {a}, Rating: {b}')
                break


            # d input (delete jersey num)
            elif menu == 'd':
                jerseynumdel = (int(input('Enter a jersey number:')))
                playerdict.pop(jerseynumdel)
                menu = str (input('Choose an option:'))


            # u input (jersey rating update)
            elif menu == 'u':
                jerseynumupdate = (int(input('Enter a jersey number:')))
                newrating = (int(input('Enter a new rating for player:')))

                playerdict[jerseynumupdate] = newrating
                menu = str (input('Choose an option:'))


            # r input (show jerseynum rating above selected)
            elif menu == 'r':
                aboverating = (int(input('Enter a rating:')))
                print ('ABOVE', aboverating)
                for a, b in sorted(playerdict.items()):
                    if b > aboverating:
                        print(f'Jersey number: {a}, Rating: {b}')
                break
            elif menu == 'q':
                break
    elif menu == 'q':
        print('ROSTER')
        for a, b in sorted(storinginitialdict.items()):
            print(f'Jersey number: {a}, Rating: {b}')


    print ()
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    print ('Choose an option:')











