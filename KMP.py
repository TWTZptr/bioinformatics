compares = 0

def kmp(string, substr):
    res = []

    n = len(string)
    m = len(substr)

    i = 0
    j = 0
    b = getUtilityInfo(string)

    while i <= n - m + j:
        (i, j) = match(i, j, string, substr)
        if (j == m):
            res.append(i - m)

        if (j == 0):
            i += 1
        else:
            i += b[1][j]
            j = b[1][j]

    return res

def getUtilityInfo(string):
    b = [0]
    bl = [0, 1]
    i = 1
    global compares

    while (i < len(string)):
        prev = b[i - 1]
        compares += 1
        if (string[prev] == string[i]):
            b.append(prev + 1)
        else:
            b.append(0)

        bl.append(b[i] + 1)
        i += 1

    return (b, bl)

def match(i, j, string, substr):
    global compares
    
    while (j < len(substr)):
        compares += 1
        if (string[i] != substr[j]):
            return (i, j)
        i += 1
        j += 1

    return (i, j)
    

print(kmp("aaaaa", "a"))
print(compares)