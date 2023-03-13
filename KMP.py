compares = 0

def kmp(string, substr):
    res = []

    n = len(string)
    m = len(substr)

    i = 0
    j = 0
    b = getUtilityInfo(substr)
    print(b)

    while i <= n - m + j:
        (i, j) = match(i, j, string, substr)
        if (j == m):
            res.append(i - m)

        if (j == 0):
            i += 1
        elif (j == m): 
            j = 0
        else:
            i += b[1][j]
            j = b[1][j]

    return res

def getUtilityInfo(string):
    global compares
    n = len(string)
    i = 1
    j = 0
    b = [0]
    bl = [0, 1]

    while (i != n):
        compares += 1
        if (string[i] == string[j]):
            b.append(j + 1)
            bl.append(j + 2)
            j += 1
            i += 1
        else:
            if (j == 0):
                b.append(0)
                bl.append(1)
                i += 1
            else:
                j = b[j - 1]

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
    

print(kmp("aabaabaaaabaabaaab", "abaab"))
# print(kmp("baabaaab", "baab"))
# print(kmp("abcabd", "abaab"))
# print(kmp("aaaaa", "a"))
print(compares)