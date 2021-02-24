def weird_arithmetic(x,y,z): #function definition
    print((x**x + y**z)//z) #code block   
weird_arithmetic(5,6,7) #function call

def myFunction(greeting,name):
    print(greeting + " " + name)
myFunction("Hello","Jacob")

def returnFunction(x):
    return x
someNumber = returnFunction(10)
print(someNumber)
print("**********Area Of Circle**************")
#AREA OF CIRCLE
def areaFunction(radius):
    PI = 3.14
    return PI*(radius**2)
r = 4
AreaOFCircle = areaFunction(4)
print(AreaOFCircle)
print("***********Volume Of Cylinder******************")
#vOLUME OF CYLINDER
def volumeFunction(radius,height):
    PI = 3.14
    return PI*radius**2*height
h = 10
VolumeOFCyl = volumeFunction(r,h)
print(VolumeOFCyl)    



