def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


try:
    while True:
        if collatz(int(input('Enter an integer: \n'))) != 1:
            continue
        else:
            break
except ValueError:
    print('Please enter an integer value e.g 1, 2')
