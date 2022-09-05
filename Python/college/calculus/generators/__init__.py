import random


def RandNumGenerator(amount):

    for i in range(amount):
        yield round(random.random()*100, 1)



if __name__ == '__main__':
    numbers = RandNumGenerator(100)
    print(numbers, type(numbers))
    for nums in numbers:
        print(nums)