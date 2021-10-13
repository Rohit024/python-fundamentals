def calc(num, k):
    a = num//k
    num = num-(a*k)
    return num, a
