
def increasingTriplet(nums) -> bool:
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

print(increasingTriplet([20,100,10,12,5,13]))