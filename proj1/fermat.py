import math
import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


# time complexity n^3
# space complexity n^2
def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.
    if y == 0: return 1
    z = int(mod_exp(x, math.floor(y / 2), N))
    if y % 2 == 0:
        return int(pow(z, 2, N))
    else:
        return int(x * pow(z, 2, N))


def fprobability(k):
    # You will need to implement this function and change the return value.
    return 1 - (1 / pow(2, k))


def mprobability(k):
    # You will need to implement this function and change the return value.
    return 1 - pow((1 / 4), k)

# time complexity n^3
# space complexity n^2
def fermat(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likely want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    hi = N - 1
    low = 1
    a_values = [random.randint(low, hi) for i in range(k)]
    for i in range(k):
        if mod_exp(a_values[i], N - 1, N) != 1:
            return 'not prime'

    return "prime"

# time complexity n^4
# space complexity n^2
def miller_rabin(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    hi = N - 1
    low = 1
    a_values = [random.randint(low, hi) for i in range(k)]
    for i in range(k):
        x = mod_exp(a_values[i], N - 1, N)
        if x == 1:
            xp = N - 1
            while x % 2 == 0:
                xp = int(x / 2)
                if xp % 2 == 0:
                    r = mod_exp(a_values[i], xp, N)
                    if r == 1 or r == (N - 1):
                        continue
                    else:
                        return 'composite'
                else:
                    return 'composite'
            return 'prime'
        else:
            return 'composite'
