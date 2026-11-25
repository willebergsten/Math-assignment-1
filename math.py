import math

#1-1
def l(x: float, y: float):
    return math.sqrt(x * x + y * y)

#1-2
def s(x: int):
    return abs(x)

#1-3
def f(n: int):
    total = 0.0
    i = 0
    while i <= n:
        total += (i * i) / n
        i += 1
    return total

#1-4
def g(n: int):
    if n < 1:
        return 0

    total = 0.0
    i = 1
    while i <= n:
        product = 1.0
        j = 1
        while j <= n:
            if j != i:
                product *= (i * j)
            j += 1
        total += (3 * i) + (n * product)
        i += 1
    return total

#1-5
def h(theta: float, x: float, y: float):
    cos_term = math.cos(theta) * (x - (x * y) * x)
    sin_term = math.sin(theta) * (y - x)
    sqrt_term = math.sqrt((x + y) * x)

    return cos_term + sin_term + sqrt_term


def tests():

    test_l1 = l(3.0, 4.0)
    print(f"l1(3.0, 4.0) = {test_l1}")
    assert test_l1 == 5.0

    test_l2 = l(0.0, 0.0)
    print(f"l2(0.0, 0.0) = {test_l2}")
    assert test_l2 == 0.0

    test_l3 = l(1.5, 4.2)
    print(f"l3(1.5, 4.12) = {test_l3}")
    assert math.isclose(test_l3, math.sqrt(19.89))

    test_s1 = s(-5)
    print(f"s1(-5) = {test_s1}")
    assert test_s1 == 5

    test_s2 = s(5)
    print(f"s2(5) = {test_s2}")
    assert test_s2 == 5

    test_s3 = s(0)
    print(f"s3(0) = {test_s3}")
    assert test_s3 == 0

    test_f1 = f(1.0)
    print(f"f1(1.0) = {test_f1}")
    assert test_f1 == 1.0

    test_f2 = f(2.0)
    print(f"f2(2.0) = {test_f2}")
    assert test_f2 == 2.5

    test_f3 = f(3.0)
    print(f"f3(3.0) = {test_f3}")
    assert math.isclose(test_f3, 1.0 / 3.0 + 4.0 / 3.0 + 9.0 / 3.0)

    test_g1 = g(0.0)
    print(f"g1(0.0) = {test_g1}")
    assert test_g1 == 0.0

    test_g2 = g(1.0)
    print(f"g2(1.0) = {test_g2}")
    assert test_g2 == 4.0

    test_g3 = g(2.0)
    print(f"g3(2.0) = {test_g3}")
    assert test_g3 == 17.0

    test_g4 = g(3.0)
    print(f"g4(3.0) = {test_g4}")
    assert test_g4 == 126.0

    test_h1 = h(0.0, 2.0, 2.0)
    print(f"h1(0.0, 2.0, 2.0) = {test_h1}")
    assert math.isclose(test_h1, -6.0 + math.sqrt(8.0))

    test_h2 = h(0.0, 1.0, 3.0)
    print(f"h2(0.0, 1.0, 3.0) = {test_h2}")
    assert math.isclose(test_h2, -2.0 + math.sqrt(4.0))

if __name__ == "__main__":
    tests()
    print("Tests passed")
