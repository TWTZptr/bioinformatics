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
        i+=1

    return result

def compare(start, m, string, substr):
    i = 0
    global compares

    compares += 1
    while (i != m and string[i + start] == substr[i]):
        compares += 1
        i += 1

    return i

print(naive("abcfababaa", "ab"))
print(compares)
