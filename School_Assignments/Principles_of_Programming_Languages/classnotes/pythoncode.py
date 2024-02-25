def gcd2(a, b):
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a
    
print(gcd2(13, 70))