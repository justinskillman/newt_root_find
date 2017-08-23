import sys

def fn(x, coeffs):
    res = 0
    for i in range(len(coeffs)):
        res = res + coeffs[i]*x**(len(coeffs) - 1 - i)
    return res

def fn_prime(x, coeffs):
    res = 0
    for i in range(len(coeffs) - 1):
        res = res + (coeffs[i]*(len(coeffs) - 1 - i))*x**(len(coeffs) - 2 - i)
    return res

def newton_method(x, coeffs, tol=0.0001):
    while True:
        if fn_prime(x, coeffs)==0:
            return x
        x1 = x - fn(x, coeffs) / fn_prime(x, coeffs)
        diff = abs(x1 - x)
        x = x1
        if diff < tol:
            break
    return x

for line in sys.stdin:
    coeffs = [int(x) for x in line.split(',')]
    init_guess = 1
    print(newton_method(init_guess, coeffs))

