pwd
ls #buscarlibreria
cd desktop
cd /mnt/
ls # todas las carpetas 
cd desktop # entrar al escritorio y buscar la imagen 
pwd 
cp/mnt/d/escritotio/00.003.jpg imagen.jpg
ls
git status 
git add
git commit-m "Agregar nuevos archivos"
git push 
vim ejemplo1

import cv2
imagen=cv2.imread('imagen.jpg')
imagen =cv2.cvtcolor(imagen,cv2.COLOR_BGR2RGB)
print (imagen shape)
print (imagen[0],[0],[0])
imagen=cv2,resize(imagen,(256,256))
cv2.imwrite('resixeimagen.jpg',imagen)
imagen= cv2.imread('imagen.jpg')
imagen = cv2,cvtColor(imagen,cv2.COLOR-BGR2GRAY)
print(imagen.shape)
print(imagen[0],[0])
cv2.imwrite(grayimagen.jpg)

imagen[0][0]-0
imagen[0][1]-0
imagen[0][0]=0

