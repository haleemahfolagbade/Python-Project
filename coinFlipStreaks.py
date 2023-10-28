# Find out how many streak of six heads or a streak of six tails comes up in a randomly generated list


import random


def flip_coin():
    # Flips coins and returns True for heads or False for tails
    return random.random() < 0.5


def get_streak_count(flips, streak_length):
    # Returns a streak of six heads or tails in the given list of flips
    current_streak = 0
    streak_count = 0
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
        else:
            current_streak = 0

        # Only increment the streak count if the current streak is equal to the streak length

        if current_streak == streak_length:
            streak_count += 1

    return streak_count


def main():
    # Simulates a coin flip streak and print the results

    # Simulates 10000 coin flips
    flips = [flip_coin() for i in range(10000)]

    # Get the longest streak of heads or tails
    streak_count = get_streak_count(flips, 6)

    print('The number of times a streak of 6 heads or tails occur is ' + str(streak_count))


if __name__ == '__main__':
    main()
