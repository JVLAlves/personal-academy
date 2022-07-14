import math
import random


def combination(n:int, x:int):
    return math.factorial(n)/(math.factorial(x) * math.factorial(n-x))

def binom(n:int, x:int, p:float):
    return combination(n , x) * (p ** x) * ((1-p) **(n-x))

def expec(n:int, p:float):
    return n * p

def varian(n:int, p:float):
    return expec(n, p)* (1-p)

def devian(n:int, p:float):
    return math.sqrt(varian(n , p))

#######################################################

def GenerateCoinLauncher(coins:int):
    coinCounter = 0
    coinsList = []
    def CoinLauncher():
        coin = ["head", "tail"]

        return random.choice(coin)

    while coinCounter <= coins:
        coinsList.append(CoinLauncher)
        coinCounter +=1

    return coinsList

def CoinTosser(times:int, coins:int):
    pounds = GenerateCoinLauncher(coins-1)
    print(len(pounds))
    x = 0
    throws = times
    CoinClipboard = {"head": 0, "tail": 0}
    while x <=throws :

        for p in pounds:
            side = p()
            CoinClipboard[side] += 1

        x += 1

        print(f"Throw {x}\t{CoinClipboard}")


if __name__ == "__main__":

    CoinTosser(100, 200)