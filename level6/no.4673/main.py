def d(a):
    return a + sum(list(map(int, list(str(a)))))

list_a = [i + 1 for i in range(10000)]

for i in range(1, 10001):
    try:
        list_a.remove(d(i))
    except:
        pass

for i in list_a:
    print(i)