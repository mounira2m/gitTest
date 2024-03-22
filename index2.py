def div(a, b):
    c = 0  # Initialize c
    if b == 0:
        print("error")
    else:
        c = a / b
    return c

a = 8
b = 4
print(a, "divided by", b, "is", div(a, b))
