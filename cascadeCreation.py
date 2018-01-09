import os, os.path
import re, shutil
import cv2, numpy as np

def clearDir():
    try:
        os.remove("wheel.info")
        print("Archivo INFO anterior eliminado")
    except:
        print("No hay INFO que borrar")
    try:
        os.remove("wheel.vec")
        print("Archivo VEC anterior eliminado")
    except:
        print("No hay VEC que borrar")
    try:
        os.remove("bg.txt")
        print("Archivo TXT anterior eliminado")
    except:
        print("No hay TXT que borrar")
    try:
        shutil.rmtree('data')
        print("Carpeta DATA anterior eliminada")
    except:
        print("No hay DATA que borrar")



def readPositivesAndChangeName():
    numForLoop = 1
    lst = os.listdir("pos")
    orderlst = sorted(lst, key=lambda x: (int(re.sub('\D','',x)),x))
    for filename in orderlst:
        os.rename("pos/"+str(filename), "pos/pos_"+str(numForLoop)+".png")
        numForLoop += 1
    print("Positivos, nombres cambiados")

def readPositivesAndChangeSize():
    for filename in os.listdir("pos"):
        img = cv2.imread("pos/"+str(filename),cv2.IMREAD_GRAYSCALE)
        resized = cv2.resize(img, (50, 50))
        cv2.imwrite("pos/"+str(filename), resized)
    print("Positivos, tamano modificado")

def writeInfoFile():
    lst = os.listdir("pos")
    orderlst = sorted(lst, key=lambda x: (int(re.sub('\D','',x)),x))
    for filename in orderlst:
        path = "pos/"+filename
        file = cv2.imread(path)
        height, width, channels = file.shape
        line = path + " 1 0 0 "+str(height)+" "+str(width)+"\n"
        with open("wheel.info", "a") as info:
            info.write(line)
    print("Positivos, Archivo INFO creado")



def readNegativesAndChangeName():
    numForLoop = 1
    lst = os.listdir("neg")
    orderlst = sorted(lst, key=lambda x: (int(re.sub('\D','',x)),x))
    for filename in orderlst:
        os.rename("neg/"+str(filename), "neg/neg_"+str(numForLoop)+".png")
        numForLoop += 1
    print("Negativos, nombres cambiados")

def readNegativesAndChangeSize():
    lst = os.listdir("neg")
    orderlst = sorted(lst, key=lambda x: (int(re.sub('\D','',x)),x))
    for filename in orderlst:
        img = cv2.imread("neg/"+str(filename),cv2.IMREAD_GRAYSCALE)
        resized = cv2.resize(img, (100, 100))
        cv2.imwrite("neg/"+str(filename), resized)
    print("Negativos, tamano modificado")

def writeBgFile():
    lst = os.listdir("neg")
    orderlst = sorted(lst, key=lambda x: (int(re.sub('\D','',x)),x))
    for filename in orderlst:
        path = "neg/"+filename+"\n"
        with open("bg.txt", "a") as bg:
            bg.write(path)
    print("Negativos, Archivo TXT creado")



def consoleCreatePositiveVec():
    num = len(os.listdir("pos"))
    firstItem = "pos/"+os.listdir("pos")[0]
    file = cv2.imread(firstItem)
    height, width, channels = file.shape
    os.popen("opencv_createsamples -info wheel.info -num "+str(num)+" -w "+str(width)+" -h "+str(height)+" -vec wheel.vec")
    print("Positivos, Archivo VEC creado")

def consoleCreateCascade():
    stages = 10

    firstItem = "pos/"+os.listdir("pos")[0]
    file = cv2.imread(firstItem)
    height, width, channels = file.shape

    numPos = (len(os.listdir("pos"))*90)/100
    numNeg = (len(os.listdir("neg"))*90)/100

    os.popen("mkdir data")
    print("Carpeta DATA creada")
    print("Ejecutar a continuacion,")
    print("opencv_traincascade -data data -vec wheel.vec -bg bg.txt -numPos "+str(numPos)+" -numNeg "+str(numNeg)+" -numStages "+str(stages)+" -w "+str(width)+" -h "+str(height))



clearDir()

readPositivesAndChangeName()
readPositivesAndChangeSize()
writeInfoFile()

readNegativesAndChangeName()
readNegativesAndChangeSize()
writeBgFile()

consoleCreatePositiveVec()
consoleCreateCascade()
