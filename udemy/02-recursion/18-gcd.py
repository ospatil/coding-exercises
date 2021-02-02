# euclidian algorithm
# gcd(a, 0) = a
# gcd(a, b) = gcd(b, a mod b)


def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers must be integers"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    print(f"gcd(48, 18) = {gcd(48, 18)}")
