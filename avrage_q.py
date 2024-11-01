def avg_q(s):
    n = len(s)
    a = [0] * n
    total = 0
    for i in range (n):
        total += s[i]
        a[i] = total / (i + 1)
    return a
