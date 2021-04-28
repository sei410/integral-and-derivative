import matplotlib.pyplot as plt
import numpy as np
import math
import sympy as sym
sym.init_printing()
Pi = sym.S.Pi # 円周率
E = sym.S.Exp1 # 自然対数の底
I = sym.S.ImaginaryUnit # 虚数単位
oo = sym.oo # 無限大
(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sym.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

def limit(Y):
    tmp = input("n → ")
    return sym.limit(Y, x, tmp)

def derivative(Y):
    return sym.diff(Y)

def integral(Y,x):
    return sym.integrate(Y, x)

expr = input("y = ")
print(expr)
print("1:極限計算")
print("2:微分")
print("3:不定積分")
print("4:定積分")
num=int(input("選択: "))

if num==1:
    ans=limit(expr)
elif num==2:
    ans = derivative(expr)
elif num==3:
    ans=integral(expr,x)
else:
    upper = input("上端: ")
    bottom = input("下端: ")
    ans = integral(expr, (x,bottom,upper))
print("解: ",ans)
