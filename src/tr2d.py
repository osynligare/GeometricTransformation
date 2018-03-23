import sys
import numpy as np
import math

def translate(vin,dx,dy):
#dx dan dy merupakan float
#vin adalah list yang menampung titik (Matriks), dx perubahan Koordinat X dan dy perubahan koordinat Y
#mengembalikan matriks baru yang berisi vin yang sudah translasi
    vertices = np.array(vin)
    for i in range(len(vertices)):
        vertices[i][0]=vertices[i][0]+dx
        vertices[i][1]=vertices[i][1]+dy
    
    return vertices

def dilate(vin,k):
#vin dilatasi dengan faktor skala k
#mengembalikan matriks baru yang berisi vin yang sudah dilatasi
    vertices = np.array(vin)
    for i in range(len(vertices)):
        vertices[i] = vertices[i]*k
       
    return vertices

def rotate(vin,deg,a,b):
#mengembalikan matriks baru yang berisi vin yang sudah dirotasi pada titik (a,b) dan deg derajat
    vertices = np.array(vin)
    for i in range(len(vin)):
        vertices[i][0] = (vin[i][0]-a)*math.cos(math.radians(deg)) - (vin[i][1]-b)*math.sin(math.radians(deg)) + a
        vertices[i][1] = (vin[i][0]-a)*math.sin(math.radians(deg)) + (vin[i][1]-b)*math.cos(math.radians(deg)) + b

    return vertices

def reflect(vin,param):
#mengembalikan matriks baru yang merupakan vin yang sudah direkfleksi dengan x,y,y=x,y=-x,atau titik (a,b)
    vertices = np.array(vin)
    par = param.split(',')
    if len(par)==2:      #param berupa titik (a,b)
        a = float(par[0][1:])
        b = float(par[1][:len(par[1])-1])
        for i in range(len(vin)):
            vertices[i][0] = 2*a-vin[i][0]
            vertices[i][1] = 2*b-vin[i][1]
    else:
        if param=='x':
            for i in range(len(vin)):
                vertices[i][1] = -vin[i][1]
        elif param=='y':
            for i in range(len(vin)):
                vertices[i][0] = -vin[i][0]
        elif param=='y=x':
            for i in range(len(vin)):
                vertices[i][0] = vin[i][1]
                vertices[i][1] = vin[i][0]
        elif param=='y=-x':
            for i in range(len(vin)):
                vertices[i][0] = -vin[i][1]
                vertices[i][1] = -vin[i][0]
    
    return vertices

def shear(vin,par,k):
#mengembalikan matriks baru yang merupakan vin yang telah digusur terhadap sumbu <par> dengan faktor gusuran <k>
    vertices = np.array(vin)
    if par=='x':
        for i in range(len(vin)):
            vertices[i][0] = vin[i][0] + k*vin[i][1]
    elif par=='y':
        for i in range(len(vin)):
            vertices[i][1] = vin[i][1] + k*vin[i][0]

    return vertices

def stretch(vin,par,k):
#mengembalikan matriks baru yang merupakan vin yang telah diregangkan terhadap sumbu <par> dengan faktor regangan <k>
    vertices = np.array(vin)
    if par=='x':
        for i in range(len(vin)):
            vertices[i][0] = vin[i][0]*k
    elif par=='y':
        for i in range(len(vin)):
            vertices[i][1] = vin[i][1]*k

    return vertices

def custom(vin,a,b,c,d):
#mengembalikan matriks baru yang merupakan vin yang telah dikalikan dengan matriks transformasi [[a,b],[c,d]]
    vertices = np.array(vin)
    mtrans = np.array([[a,b,0],[c,d,0],[0,0,0]])

    return vertices.dot(mtrans)

def multiple(vin,n):
#Melakukan transformasi linier pada vin sebanyak n kali berurutan.
#Setiap baris input 1..n dapat berupa translate, rotate, shear, dll tetapi bukan multiple, reset, exit
    vertices = np.array(vin)
    for i in range(n):
        inp = input('masukan fungsi ke-%d : '%(i+1))
        trans = inp.split(' ')
        if trans[0] == "translate":
            vertices = translate(vertices,float(trans[1])/200,float(trans[2])/200)
        elif trans[0] == "dilate":
            vertices = dilate(vertices,float(trans[1]))
        elif trans[0] == 'rotate':
            vertices = rotate(vertices,float(trans[1]),float(trans[2])/200,float(trans[3])/200)
        elif trans[0] == 'reflect':
            vertices = reflect(vertices,trans[1])
        elif trans[0] == 'shear':
            vertices = shear(vertices,trans[1],float(trans[2]))
        elif trans[0] == 'stretch':
            vertices = stretch(vertices,trans[1],float(trans[2]))
        elif trans[0] == 'custom':
            vertices = custom(vertices,float(trans[1]),float(trans[2]),float(trans[3]),float(trans[4]))
        elif trans[0] == 'exit':
            print("SAMPAI JUMPA ;)")
            sys.exit()

    return vertices