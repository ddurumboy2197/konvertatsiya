def matris_kopaytir(matr1, matr2):
    if len(matr1[0]) != len(matr2):
        return "Matrislar ko'paytirish uchun mos emas"
    
    natija = [[0 for _ in range(len(matr2[0]))] for _ in range(len(matr1))]
    
    for i in range(len(matr1)):
        for j in range(len(matr2[0])):
            for k in range(len(matr2)):
                natija[i][j] += matr1[i][k] * matr2[k][j]
    
    return natija

matr1 = [[1, 2], [3, 4]]
matr2 = [[5, 6], [7, 8]]

print(matris_kopaytir(matr1, matr2))
