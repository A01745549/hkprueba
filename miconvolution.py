git add
git ls
touch miconvolution.py
ls
git status
git add miconvolution.py
git commit -m "hola"
vim mi convolucion.py
#funcion que calcula la matriz resultante C despues de aplicar la operacion convolucion de a*b

def convolucion(A,B):
    C = np.zeros((len(A)-2,len(A[0])-2))
    n = 0
    for i in range(len(C)):
        for j in range(len(C[0])):
            resultado = 0
            for iaux in range(len(B)):
                for jaux in range(len(B[0])):
                    resultado += A[i+iaux][j+jaux]*B[iaux][jaux]
            C[i][j] = resultado
    return C

matriz1=[[6,9,0,3].[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro=[[1,0,2],[5,0,9],[6,2,1]]
esc:wq
python3 miconvolucion.py
pip3 install numpy 
python3
import numpy 
import numpy as np
def convolucion()
C=0
return C
matriz1=[[6,9,0,3].[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro=[[1,0,2],[5,0,9],[6,2,1]]
A=np.array(matriz1)
B=np.array(filtro)

print(A[1],[0])
print(C)
print(A)
esq:wq

