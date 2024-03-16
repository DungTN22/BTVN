import numpy as np
import math as m
import random as r
'''
print(np.linspace(0,10,7))
print(np.arange(0,10,3))

matrix1=np.array([[1,2,3],[4,5,6]])
print(matrix1)
print(np.shape(matrix1))
print(np.shape(matrix1)[0])
print(np.shape(matrix1)[1])
print(np.size(matrix1))
print(np.ndim(matrix1))


matrix2=np.array([[3,1,9,0],[7,8,4,2]])
k=np.sort(matrix2,axis=1)
print(k)


matrix3a=np.array([[2,4,6,8],[3,5,7,9]])
matrix3b=np.array([[1,2,3,4],[5,6,7,8]])
a1=np.concatenate((matrix3a,matrix3b),axis=0)
print(a1)
b1=np.concatenate((matrix3a,matrix3b),axis=1)
print(b1)
a2=np.hstack((matrix3a,matrix3b))
print(a2)
b2=np.vstack((matrix3a,matrix3b))
print(b2)



matrix4=np.arange(0,20,3)
print(matrix4)
tach=np.split(matrix4,(2,4,6))
print(tach)

print(np.reshape(matrix4,(7,1)))




matrix5a=np.array([[4,2],[7,1]])
matrix5b=np.array([[6],[2]])
matrix5c=np.array([[0,8],[1,3]])
print(matrix5a+matrix5c)
print(matrix5a-matrix5c)
print(np.multiply(matrix5a,matrix5b))
print(np.divide(matrix5a,matrix5b))

matrix6=np.array([[1,6,3],[2,5,6],[7,8,0]])

det=np.linalg.det(matrix6)
print(det)
nghichdao=np.linalg.inv(matrix6)
print(nghichdao)
chuyenvi=np.transpose(matrix6)
print(chuyenvi)
lonnhat=np.max(matrix6)
print(lonnhat)
trungbinh=np.mean(matrix6)
print(trungbinh)


print(m.pi)
print(m.fabs(-10))
print(m.pow(9,2))
print(m.sqrt(9))
print(m.factorial(5))
print(m.exp(4))
print(m.gcd(8,6))
print(m.hypot(3,4))
print(m.prod([1,2,3,5,9]))
print(m.log(32,2))
print(m.cos(m.pi/6))
print(m.sin(m.pi/6))
print(m.tan(m.pi/4))
print(m.radians(m.pi/12))
print(m.degrees(1.3))


for i in range(4):
    print(r.random(),end=' ')
print()
for i in range(1,8,2):
    print(r.randint(0,10),end=' ')
print()
for i in range(3,7):
    print(r.uniform(5,20),end=' ')
print()
set1=set([3,1,6,3,8,0,2])
print(r.choice(list(set1)))
list2=[1,2,3,4,5,6,7,8,9,0]
r.shuffle(list2)
print(list2)
list2.sort()
print(list2)
print(r.sample(list2,5))




class graph:
    def __init__ (self,dothi):
        if dothi is None:
            self.dothi=[]
        else: self.dothi=dothi
    def chendinh(self,dinh):
        if dinh in self.dothi:
            print("đỉnh đã tồn tại")
        else: self.dothi[dinh]=[]
    def chencanh(self,dinh,canh):
        if canh not in self.dothi[dinh]:
            self.dothi[dinh].append(canh)
        else:
            print("đã tồn tại")
    def duyetcanh(self):
        caccanh=[]
        for key in self.dothi: 
            for value in self.dothi[key]:
                if {key,value} not in caccanh:
                    caccanh.append({key,value})
        return caccanh

l={"a":["b","d"],
   "b":["a","c","e"],
   "c":["e","b","d"],
   "d":["c","a"]
   }
dothi1=graph(l)
dothi1.chendinh("f")
dothi1.chencanh("f","a")
dothi1.chencanh("f","d")
print(dothi1.duyetcanh())


list1=[["dũng","thư"],["tùng","hạnh"],["quang","lan"],["huy","ngân"]]
dict1=dict(list1)
dict2={"tình":"yêu",
       "họ":"hàng",
       "nhà":"nước",
       "công":"an"}
print(dict1,dict2)
dict2["nhện"]="tơ"
print(dict2)
dict1.update(dict2)
print(dict1)
dict2.update(công="tơ")
print(dict2)
'''