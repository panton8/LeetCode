def numWaterBottles(numBottles: int, numExchange: int) -> int:
    bottles_of_water = numBottles

    while numBottles // numExchange >= 1:
        remains = numBottles % numExchange
        numBottles //= numExchange
        bottles_of_water += numBottles
        numBottles += remains

    return bottles_of_water
