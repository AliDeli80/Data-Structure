def unique(s):
    n = len(s)
    for i in range (n):
        for j in range (i + 1 , n):
            if (s[i] == s[j]):
                return False
    return True