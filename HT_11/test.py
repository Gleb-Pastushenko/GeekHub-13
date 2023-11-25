result = 0

a = 2
b = 3

def res(a, b):
    global result
    return result := a + b

res(a, b)