# find sum of two fractions

def find_gcd(b, d):
    if not d:
        return b
    else:
        return find_gcd(d, b % d)


def get_fractions(a_b, c_d):
    a_pos = a_b.find('/')
    c_pos = c_d.find('/')

    a = int(a_b[:a_pos])
    b = int(a_b[a_pos + 1:])
    c = int(c_d[:c_pos])
    d = int(c_d[c_pos + 1:])

    gcd = find_gcd(b, d)

    c *= b / gcd
    a *= d / gcd
    den = b * d / gcd

    s = a + c
    gcd = find_gcd(s, den)

    s = int(s / gcd)
    den = int(den / gcd)

    return "{}/{}".format(s, den)


if __name__ == '__main__':
    assert get_fractions('1/4', '3/16') == '7/16'
    assert get_fractions('5/4', '1/4') == '3/2'
    assert get_fractions('1/7', '5/13') == '48/91'
