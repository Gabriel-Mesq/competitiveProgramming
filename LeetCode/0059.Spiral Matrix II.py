class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matriz = [[0] * n for i in range(n)]

        valor = 1
        topo, esquerda = 0, 0
        baixo, direita = n - 1, n - 1

        while topo <= baixo and esquerda <= direita:

            for _ in range(topo, direita + 1):
                matriz[topo][_] = valor
                valor += 1

            topo += 1
            
            for _ in range(topo, direita + 1):
                matriz[_][direita] = valor
                valor += 1

            direita -= 1

            for _ in range(direita, esquerda - 1, -1):
                matriz[baixo][_] = valor
                valor += 1

            baixo -= 1

            for _ in range(baixo, topo - 1, -1):
                matriz[_][esquerda] = valor
                valor += 1

            esquerda += 1
        
        return matriz

