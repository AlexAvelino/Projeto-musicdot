def SumDistinctOdds(numbers):
    numbers = list(set(numbers))
    sumOdds = 0
    for i in range(len(numbers)):
        if (numbers[i] % 2 != 0):
            sumOdds += numbers[i]

    return sumOdds


numbers = [1,1,2,2,3]
print(SumDistinctOdds(numbers))