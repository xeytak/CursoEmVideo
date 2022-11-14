d = 12.5
e = 'teste'
def isNumber(n):
    try:
        float(n)
    except ValueError:
        return False
    return True
b = isNumber(4.5)
print(b)