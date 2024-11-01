def avg(s):
    n = len(s)
    a = [0] * n
    for i in range (n):
        total = 0
        for j in range (i + 1):
            toral += s[j]
        a[i] = total/(i + 1)
    return a