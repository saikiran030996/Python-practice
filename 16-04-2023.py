# instance variables accessing

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def display(self):
        print(self.a)
        print(self.b)

t = Test()
t.display()
print(t.a)
print(t.b)

#-----------------------------------------------------
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.c 
        del self.d

    def m2(self):
        self.e = 50
        self.f = 60

t1 = Test()
t1.m1()
#t1.m2()
print(t1.__dict__)
#------------------------------------------------------------
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.c 
        del self.d

    def m2(self):
        self.e = 50
        self.f = 60

t1 = Test()
#t1.m1()
#t1.m2()
t2 = Test()
t2.m2()
del t2.b,t2.d
print(t1.__dict__)
print(t2.__dict__)
#--------------------------------------------------------------------

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
t1 = Test()
t1.a = 888
t1.b = 999

t2 = Test()

print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
#------------------------------------------
class Test:
    a = 10

print(Test.__dict__)
#--------------------------------------------

class Test:
    a = 10
    def __init__(self):
        Test.b = 20
    def m1(self):
        Test.c = 40
    @classmethod
    def m2(cls):
        cls.d = 40
        Test.e = 50
    @staticmethod
    def m3():
        Test.f = 60

t = Test()
t.m1()
Test.m2()
Test.m3()
Test.g = 70
print(Test.__dict__)
#----------------------------------------------------
class Test:
    a = 10
    def __init__ (self):
        print(self.a)
        print(Test.a)
    def m1(self):
        print(self.a)
        print(Test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        print(Test.a)

t = Test()
t.m1()
Test.m2()
Test.m3()
print(t.a)
print(Test.a)

class Test:
    a = 10
    def __init__(self):
        Test.a = 20

    def m1(self):
        Test.a = 30
    
    @classmethod
    def m2(cls):
        cls .a = 40
        Test.a = 50
    @staticmethod
    def m3():
        Test.a = 60


t = Test()
t.m1()
Test.m2()
Test.m3()
print(Test.a)
Test.a = 70
#------------------------------------------------------------------------------------------------------------

#Example1
class Test:
    a = 10
    def m1(self):
        self.a = 888

t1 = Test()
t1.m1()
print(Test.a)
print(t1.a)

#Example2

class Test:
    a = 10
    def m1(self):
        Test.a = 888

t1 = Test()
t1.m1()
print(Test.a)
print(t1.a)

#Example2

class Test:
    a = 10
    def __init__(self):
        self.b = 20

t1 = Test()
t2 = Test()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
t1.a = 888
t1.b = 999
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)


# Example3

class Test:
    a = 10
    def __init__(self):
        self.b = 20

t1 = Test()
t2 = Test()
print(t1.a,t1.b)
print(t2.a,t2.b)
Test.a = 888
Test.b = 1000
print(t1.a,t1.b)
print(t2.a,t2.b)
print(Test.a,Test.b)