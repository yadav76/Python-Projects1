# calculating sum of n numbers using recursive function

def sumOf(n):

    sum = 0
    for i in range(n):
        sum = sum + (i+1)

    return sum

def recurse(n):

    return n+sumOf(n-1)

f = recurse(9)
print(f)
