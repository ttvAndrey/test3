from math import pi
class Kalkulator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def clojenie(self):
        d=a+b
        return d
    def vichitanie(self):
        f=a-b
        return f
    def umnojenie(self):
        g=a*b
        return g
    def delenie(self):
        if b == 0:
            print("Деление не возможно")
            return"Ошибка"
        h=a/b
        return h
    def procent(self):
        j=a%b
        return j
    '''
    def inversyi(self):
        if a==0 and b==0:
            return a,b 
        k=0
        n=0        
        if a<0:
            k=a*-2+a
        else:
            k=a-a*2
        if b<0:
            n=b*-2+b
        else:
            n=b-b*2
        return k,n
    '''
    def inversyi(self):
        return a-2*a,b-2*b        
    def ctepen(self,s1=2,s2=2):
        l=a**s1
        m=b**s2
        return l,m
while True:
    a=int(input("Введите любое число! "))
    b=int(input("Введите любое число! "))
    print("Выберите одну из операций:\n"\
        "Сложение(+)\n"\
        "Вычитание(-)\n"\
        "Умножение(*)\n"\
        "Деление(/)\n"\
        "Процент(%)\n"\
        "Степень(**)\n"\
        "Степень2(**2)\n"\
        "Инверсия(~)\n")
    op=input("Введите любую операцию")
    pop=Kalkulator(a,b)
    if op=="+":
        hj=pop.clojenie()
        print(hj)
    elif op=="-":
        jhg=pop.vichitanie()
        print(jhg)
    elif op=="*":
        ho=pop.umnojenie()
        print(ho)
    elif op=="/":
        jhp=pop.delenie()
        print(jhp)
    elif op=="%":
        i=pop.procent()
        print(i)
    elif op=="**":
        a=int(input("Введите степень первого числа! "))
        b=int(input("Введите степень второго числа! "))
        q=pop.ctepen(a,b)
        print(q[0],q[1])
    elif op =="**2":
        q=pop.ctepen()
        print(q[0],q[1])
    elif op=="~":
        t=pop.inversyi()
        print(t[0],t[1])
    elif op=="end":
        break
    