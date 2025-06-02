def f(x):
    return x**3-1

def obliczenie(a,b,c):
    print(f"dane -> a:{a}, b: {b}, c: {c}, wynik funkcji f(x) = x^3-1 -> {f(a)}")
    # yield a+b
    # yield c*a
    return (a+b)*c + f(a)

