class Ordenacao():

    def ordena(array_para_ordenar: list):
        n = len(array_para_ordenar)

        for i in range(n):
            for j in range(0, n - i - 1):
                if array_para_ordenar[j] > array_para_ordenar[j + 1]:
                    array_para_ordenar[j], array_para_ordenar[j + 1] = array_para_ordenar[j + 1], array_para_ordenar[j]
        
        # print(array_para_ordenar)
        return array_para_ordenar

    def to_string(array_ordenado: list):
        array_formatado = ""
        for i in array_ordenado:
            if array_ordenado.index(i) > 0:
                array_formatado += f", {str(i)}"
            else: 
                array_formatado += str(i)
                
        # print(array_formatado)
        return array_formatado
    
Ordenacao.ordena([4, 3, 2, 1, 5])
Ordenacao.to_string([1, 2, 3, 4, 5])
