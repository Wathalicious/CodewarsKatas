def high_and_low(numbers):
    x = numbers.split()
    y = []
    for i in x:
       y.append(int(i))
    
    nums = (str(max(y)) + " " + str(min(y)))
    print(nums)
    return nums