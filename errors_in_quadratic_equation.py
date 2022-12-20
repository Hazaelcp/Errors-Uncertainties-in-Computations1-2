#Write a program that computes the four solutions for arbitrary values a; b and c.
from math import*

a=1
b=1
c=float(input('Digite el valor de c:  '))
f1=[]
f2=[]
print('\t\t\tPrimera formula')
def formula1(a,b,c):
    dscte=b**2-4*a*c
    x=-b/(2*a)
    if dscte>0:
        x1=(-b+sqrt(dscte))/(2*a)
        x2=(-b-sqrt(dscte))/(2*a)
        f1.append(x1)
        f1.append(x2)
        print('La primera raiz es ',x1)
        print('La segunda raiz es ',x2)
    if dscte==0:
        print('La segunda raiz es ',x,' con multiplicidad 2')
    if dscte<0:
        dscte*=-1
        x1i=+sqrt(dscte)/(2*a)
        x2i=-sqrt(dscte)/(2*a)
        if x1i>0:print('La primera raiz es ',x,'+',x1i,'i')
        else:print('La primera raiz es ',x,x1i,'i')
        if x2i>0:print('La segunda raiz es ',x,'+',x2i,'i')
        else:print('La segunda raiz es ',x,x2i,'i')
print(formula1(a,b,c))
print('\t\t\tSegunda formula')
def formula2(a,b,c):
    dscte=b**2-4*a*c
    if a==0:
        print('ecuacion lineal')
        print(f'La solucion es {-c/b}')
    if c==0:
        print('La primera raiz es 0')
        print(f'La segunda raiz es {-b/a}')
    if dscte>0:
        x1=(-2*c)/(b+sqrt(dscte))
        x2=(-2*c)/(b-sqrt(dscte))
        f2.append(x1)
        f2.append(x2)
        print(f'La primera raiz es {x1}')
        print(f'La segunda raiz es {x2}')
    if dscte==0:
        x1=(-2*c)/b
        print(f'La primera raiz es {x1} con multiplicidad 2')  
    if dscte<0:
        dscte*=-1
        k=(-2*c)/(b**2 + dscte)
        re=k*b
        im=k*sqrt(dscte)
        print(f'La primera raiz es {re}+{im}i')
        print(f'La segunda raiz es {re}-{im}i')
print(formula2(a,b,c))
print('\t\t\tComparacion')
def comparar():
    print(f'Diferencia de la primera solucion {abs(f1[0]-f2[0])}')
    print(f'Diferencia  de la segunda solucion {abs(f1[1]-f2[1])}')
print (comparar())