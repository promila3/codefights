def matrixElementsSum(matrix):
    rows = len(matrix)
    totprice = 0
    if rows > 0 :
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 0 :
                    if i == 0 :
                        totprice += matrix[i][j]
                    else :
                        check = False
                        for k in range(i) :
                            if matrix[k][j] == 0:
                                check = True
                                break
                                
                        if check == False :
                            totprice += matrix[i][j]
    return totprice
