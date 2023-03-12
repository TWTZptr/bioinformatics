compares = 0

def naive(string, substr):
    result = []
    n = len(string)
    m = len(substr)

    i = 0

    while (i <= n - m):
        j = compare(i, m, string, substr)
        if (j == m):
            result.append(i)
        i += 1

    return result

def compare(start, m, string, substr):
    i = 0
    global compares

    while (i != m):
        compares += 1
        if (string[i + start] != substr[i]):
            return i
        
        i += 1

    return i

print(naive("abcfbabcaac", "abc"))
print(compares)
