pa = True
results = []
while pa:
    try:
        nf, nc = [int(x) for x in input().split(' ')]
        map1 = []
        cant = 0
        for _ in range(nf):
            f = [str(x) for x in input().split('')]
            map1.append(f)
        i = 0
        j = 0
        parada1 = False
        lenI = len(map1)
        while not parada1:
            parada2 = False
            lenJ = len(map1[i])
            while not parada2:
                n = map1[i][j]
                cond1 = False
                cond2 = False
                if n == '-':
                    if j > 0:
                        izq = map1[i][j - 1]
                        if izq != '-':
                            cond1 = True
                    if i > 0:
                        if map1[i - 1][j] != '-':
                            cond2 = True

                    if cond1 and cond2:
                        cant += 1

                j += 1
                if j >= lenJ:
                    parada2 = True
            i += 1
            if i >= lenI:
                parada1 = True

        results.append(cant)
    except:
        pa = False

for i in range(len(results)):
    print(f'Case {i + 1}: {results[i]}')
