class Ordenacao():

    # Ordena o conteúdo do array recebido como parâmetro
    def ordena(self, array_para_ordenar: []): # type: ignore

        n = len(array_para_ordenar)

        # Bubble Sort
        for i in range(n):
            for j in range(0, n - i - 1):
                if array_para_ordenar[j] > array_para_ordenar[j + 1]:
                    array_para_ordenar[j], array_para_ordenar[j + 1] = (
                        array_para_ordenar[j + 1],
                        array_para_ordenar[j]
                    )

        return array_para_ordenar

    # Converte o conteúdo do array em cadeia formatada
    def to_string(self, array_ordenado: []): # type: ignore

        array_formatado = ""

        for i in range(len(array_ordenado)):

            if i > 0:
                array_formatado += ","

            array_formatado += str(array_ordenado[i])

        return array_formatado