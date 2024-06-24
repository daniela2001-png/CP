"""

Aplicacion de la exponenciacion binaria
en la sucesion de fibonacci mediante matrices.

Para poder hallar el n-esimo termino de 
la serie con una complejidad de O(log(n))

fuente: 
"""

# Matriz Q o matriz de fibonacci
Q = [[1, 1], [1, 0]]


def multiplicar_matriz(A, B):
    if len(A[0]) != len(B):
        """
        Validamos si el núumero de columnas de A
        es igual al número de filas de B.
        """
        print("ERROR: valide bien sus matrices")
    else:
        filas_A = len(A)
        columnas_B = len(B[0])

        result = []
        """
        Creamos una matriz inicializada en ceros
        con las mismas dimensiones de A y B
        (result)
        """
        for fila in range(filas_A):
            fila = []
            for columna in range(columnas_B):
                fila.append(0)
            result.append(fila)
        """
        Realizamos la multiplicacion de las matrices A y B,
        iterando sobre las filas y columnas
        y guardamos los resultados en la nueva matriz (result)
        """
        for fila in range(filas_A):
            for columna in range(columnas_B):
                for valor in range(len(B)):
                    result[fila][columna] += A[fila][valor] * B[columna][valor]
        return result


def exponenciacion_binaria_matriz(matriz, n):
    """
    Calculamos mediante el algoritmo
    de exponenciacion binaria
    la matriz fibonacci resultante, para poder optimizar
    el numero de multiplicaciones de las matrices.
    """
    while n > 0:
        if n % 2 == 1:
            result = multiplicar_matriz(Q, matriz)
        matriz = multiplicar_matriz(matriz, matriz)
        n = n // 2
    return result


def enesimo_valor_fibonacci(n):
    """
    Obtenemos el resultado final
    """
    if n <= 1:
        return n
    resultado_matriz = exponenciacion_binaria_matriz(Q, n - 1)
    # obtenemos el valor de F(n+1)
    return resultado_matriz[0][0]


n = 6
print(f"El {n}-ésimo número de Fibonacci es: {enesimo_valor_fibonacci(n)}")
