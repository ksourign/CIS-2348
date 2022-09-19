#Kaitlyn Sourignosack
#1824497

def exact_change(user_total):
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    countingtotal = 0

#dollars
    while (countingtotal != user_total):

        if (countingtotal + 100) > user_total:
            break

        if (countingtotal + 100) == user_total:
            countingtotal += 100
            num_dollars += 1
            break

        if (countingtotal + 100) < user_total:
            countingtotal += 100
            num_dollars += 1
#quarters
    while   (countingtotal != user_total):

        if (countingtotal + 25) > user_total:
            break
        if (countingtotal + 25) == user_total:
            countingtotal += 25
            num_quarters += 1
            break

        if (countingtotal + 25) < user_total:
            num_quarters += 1
            countingtotal += 25
#dimes
    while (countingtotal != user_total):

        if (countingtotal + 10) > user_total:
            break

        if (countingtotal + 10) == user_total:
            countingtotal += 10
            num_dimes += 1
            break

        if (countingtotal + 10) < user_total:
            countingtotal += 10
            num_dimes += 1
#nickels
    while (countingtotal != user_total):

        if (countingtotal + 5) > user_total:
            break
        if (countingtotal + 5) == user_total:
            countingtotal += 5
            num_nickels += 1
            break
        if (countingtotal + 5) < user_total:
            countingtotal += 5
            num_nickels += 1
#pennies
    while (countingtotal != user_total):

        if (countingtotal + 1) > user_total:
            break

        if(countingtotal + 1) == user_total:
            countingtotal += 1
            num_pennies += 1
            break

        if (countingtotal + 1) < user_total:
            countingtotal += 1
            num_pennies += 1
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

#outputting
if __name__ == '__main__':
    input_val = int(input())

    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars == num_quarters == num_dimes == num_nickels == num_pennies == 0:
        print('no change')

    if num_dollars > 1:
        print(num_dollars, 'dollars')
    elif num_dollars == 1:
        print(num_dollars, 'dollar')

    if num_quarters > 1:
        print(num_quarters, 'quarters')
    elif num_quarters == 1:
        print(num_quarters, 'quarter')

    if num_dimes > 1:
        print(num_dimes, 'dimes')
    elif num_dimes == 1:
        print(num_dimes, 'dime')

    if num_nickels > 1:
        print(num_nickels, 'nickels')
    elif num_nickels == 1:
        print(num_nickels, 'nickel')

    if num_pennies > 1:
        print(num_pennies, 'pennies')
    elif num_pennies == 1:
        print(num_pennies, 'penny')













