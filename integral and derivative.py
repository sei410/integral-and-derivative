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

def limit():
    print("y = ")
    expr = input()
    Y = sym.Eq(expr)
    print(sym.limit(2 ** (3 * x - 1) / (Y ** 2), x, oo))

def integral():
    print("y = ")
    expr = input()
    Y = sym.Eq(expr)

def derivative():
    print("y = ")
    expr = input()
    Y = sym.Eq(expr)

