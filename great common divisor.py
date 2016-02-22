def gcd(a, b):
    if a == 0:
        x = b
        return x
    if b == 0:
        x =a
        return x
    if a>=b:
        x = gcd(a%b,b)
        return x
    if b>=a:
        x = gcd(a,b%a)
        return x