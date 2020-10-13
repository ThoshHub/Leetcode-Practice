# https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

def shapeArea(n):
    if n==1:
        return 1
    return ((n+n-1)**2) - (n*2*((n-1)))

print(shapeArea(100))