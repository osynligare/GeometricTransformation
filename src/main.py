from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
from tr2d import *
import numpy as np
import serial
import os
import sys
import time

ESCAPE = '\033'
 
 
def InitGL(Width, Height): 
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClearDepth(1.0) 
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)   
    
def GLSwindow():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)

    window = glutCreateWindow(b'OpenGL Python Cube')

    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    InitGL(600, 600)
    glutMainLoop()

def drawsumbu():
    glColor3f(0.94,0.81,0.99)

    glLineWidth(0.001); 
    glBegin(GL_LINES)
    i=-2.5
    while (i<=2.5):
        glVertex3f(float(i), -2.5, 0.0)
        glVertex3f(float(i), 2.5, 0.0)
        glVertex3f(-2.5, float(i), 0.0)
        glVertex3f(2.5, float(i), 0.0)
        i=i+0.1
    glEnd()
    glColor3f(0.87,0.58,0.98) 
    glLineWidth(0.005); 
    glBegin(GL_LINES)
    i=-2.5
    while (i<=2.5):
        glVertex3f(float(i), -2.5, 0.0)
        glVertex3f(float(i), 2.5, 0.0)
        glVertex3f(-2.5, float(i), 0.0)
        glVertex3f(2.5, float(i), 0.0)
        i=i+0.5
    glEnd()

    glColor3f(0.73,0.16,0.96)
    glBegin(GL_LINES)
    glVertex3f(0.0, -2.5, 0.0)
    glVertex3f(0.0, 2.5, 0.0)
    glVertex3f(-2.5, 0.0, 0.0)
    glVertex3f(2.5, 0.0, 0.0)
    glEnd()

def input_titik():
    global vertices
    
    global default
    print("--------------SELAMAT DATANG--------------- ")
    
    N = int(input('Masukkan jumlah titik sudut : '))
    vertices = [] #list of float
    
    for i in range (N):
        vertices.append([])
        inp = input('(x%d,y%d) '% (i+1,i+1))
        point = inp.split(',')
        vertices[i].append(float(point[0])/200)
        vertices[i].append(float(point[1])/200)
        vertices[i].append(0.0)
    
    default = np.array(vertices)
    vertices = np.array(vertices)

def DrawShape():
    global vertices

    glColor3f(0.22,0.69,0.87)
    glBegin(GL_POLYGON)
    for vertice in vertices:
        glVertex3fv(vertice)
    glEnd()
    glutSwapBuffers()

def DrawGLScene():
    global vertices
    global ct
    global trf
    global scale
    global default
    global rot
    global trans
    global degAnim
    global pertama
    global t

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(600)/float(600), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0,0.0,-6.0)    
    
    drawsumbu()
    
    DrawShape()

    if pertama>1:
        
        if (ct==101):
            input_function()
        else:
            if (ct==1):
                if (rot):
                    degAnim = float(trans[1])/100
                else:
                    scale = np.array(trf)
                    for i in range(len(scale)):
                        scale[i][0] = (trf[i][0]-vertices[i][0])/100
                        scale[i][1] = (trf[i][1]-vertices[i][1])/100
        
            if (rot):
                vertices = rotate(vertices,degAnim,float(trans[2])/200,float(trans[3])/200)
            else:
                for i in range(len(vertices)):
                    vertices[i][0] = vertices[i][0] + scale[i][0]
                    vertices[i][1] = vertices[i][1] + scale[i][1]
    
        ct = ct+1
    
    elif pertama == 1:
        input_titik()
    
    time.sleep(0.003)
    pertama = pertama+1

def input_function():
    global rot
    global ct
    global trf
    global trans
    global vertices


    rot = False
    ct = 0
    inp = input("Masukan fungsi : ")
    trans = inp.split(' ')
    if trans[0] == "translate":
        trf = translate(vertices,float(trans[1])/200,float(trans[2])/200)
    elif trans[0] == "dilate":
        trf = dilate(vertices,float(trans[1]))
    elif trans[0] == 'rotate':
        trf = rotate(vertices,float(trans[1]),float(trans[2])/200,float(trans[3])/200)
        rot = True
    elif trans[0] == 'reflect':
        trf = reflect(vertices,trans[1])
    elif trans[0] == 'shear':
        trf = shear(vertices,trans[1],float(trans[2]))
    elif trans[0] == 'stretch':
        trf = stretch(vertices,trans[1],float(trans[2]))
    elif trans[0] == 'custom':
        trf = custom(vertices,float(trans[1]),float(trans[2]),float(trans[3]),float(trans[4]))
    elif trans[0] == 'multiple':
        trf = multiple(vertices,int(trans[1]))
    elif trans[0] == 'reset':
        trf = default
    elif trans[0] == 'exit':
        print("SAMPAI JUMPA ;)")
        sys.exit()

def main():
    global vertices    
    global window
    global ct
    global pertama
    global t
    
    pertama = 0

    vertices=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
    ct = 101
    GLSwindow()

 
if __name__ == "__main__":
    main()
