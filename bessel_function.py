#Write a program that uses the backward recursion formulas
#up (up) and down (down) to calculate bessel functions for the
#first 25 values of l for x = 0:1; 1; 10.

from math import*
l=60
vec=[0.1,1,10]
lista1=[]
lista2=[]

def besselup(l,x,lista1):
    j0=sin(x)/x
    j1=sin(x)/(x**2)-cos(x)/x
    lista1.append(j0)
    lista1.append(j1)

    for i in range(2,26):
        js=((2*i-1)/x)*j1-j0
        j0=j1
        j1=js
        lista1.append(js)
    return 0
def besseldown(l,x,lista2):
    jL=0.05
    jL_1=0.025
    j0=sin(x)/x
    j1=sin(x)/(x**2)-cos(x)/x
    lista=[]
    lista2.append(j0)
    lista2.append(j1)
    for i in range(l,-1,-1):
        js=((2*i+3)/(x))*jL_1 - jL
        jL=jL_1
        jL_1=js
        lista.append(js)
    lista.reverse()
    for i in range(2,26):
        v=(lista[i])*(j0/lista[0])
        lista2.append(v)
    return 0
def comparar(lista1, lista2):
    print('\n\t\t\t\t\tComparación para x=0.1')
    print('{:^25}{:^25}{:^25}{:^25}'.format('l','jl up','jl down','comparación'))
    print('\n')

    for i in range(0,26):
        c=abs(lista1[i]-lista2[i])/(abs(lista1[i])+abs(lista2[i]))
        print('{:^25}{:^25}{:^25}{:^25}'.format(i,lista1[i],lista2[i],c))

    print('\n\t\t\t\t\tComparación para x=1')
    print('{:^25}{:^25}{:^25}{:^25}'.format('l','jl up','jl down','comparación'))
    print('\n')

    for i in range(26,52):
        c=abs(lista1[i]-lista2[i])/(abs(lista1[i])+abs(lista2[i]))
        print('{:^25}{:^25}{:^25}{:^25}'.format(i-26,lista1[i],lista2[i],c))

    print('\n\t\t\t\t\tComparación para x=10')
    print('{:^25}{:^25}{:^25}{:^25}'.format('l','jl up','jl down','comparación'))
    print('\n')

    for i in range(52,78):
        c=abs(lista1[i]-lista2[i])/(abs(lista1[i])+abs(lista2[i]))
        print('{:^25}{:^25}{:^25}{:^25}'.format(i-52,lista1[i],lista2[i],c))

    return 0

for i in range(0,len(vec)):
    print(besselup(l,vec[i],lista1))
for i in range(0,len(vec)):
    print(besseldown(l,vec[i],lista2))

print(comparar(lista1,lista2))
