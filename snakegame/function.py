
#def assignment(a, b):
def assignment(n)
   # check which number is bigger.

    # squer the bigger nuber,
    # trible the smaller number

    # calculate the sum of the ther squar and trible result.

    #c = a * a + b * 2
    c = n[0] * n[0] + n[1] * 2

    return c

numbers = [
    [2, 3],
    [4, 5],
    [5, 6],
    [10, 6]
]

for num in numbers:
    
    #result = assignment(num[0], num[1])
    result = assignment(num)

    print(result)