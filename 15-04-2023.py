class movie:
    '''Movie class developed by Durga for python demo purpose'''
    def __init__(self,title,hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine
    
    def info (self):
        print('Movie name:',self.title)
        print('Hero name:',self.hero)
        print('Heroine name:',self.heroine)

list_of_movies = []
while True:
    title = input('Enter Movie name:')
    hero = input('Enter hero name:')
    heroine = input('Enter heroine name:')
    m = movie(title,hero,heroine)
    list_of_movies.append(m)
    print('Movie added successfully')
    option =  input('Do you want to add more movies [yes/No]:')
    if option.lower() =='no':
        break


class Test:
    def Test(self):
        print('It is some special method')

t = Test()
t.Test()

--------------------------------------------------------------------------------------------------

# class method

class Test:
    @classmethod
    def m1(cls):
        print(id(cls))

print(id(Test))
Test.m1()


# Types of Methods

class Student:
    schoolname = 'DURGASOFT'
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def getstudentInfo(self):
        print('Student Name:',self.name)
        print('Student Rollno:',self.rollno)
    @classmethod
    def getSchoolName(cls):
        print('School Name:',cls.schoolname)
    @staticmethod
    def getSum(a,b):
        sum = a+b
        return sum 

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30
        self.d = 40

t1 = Test()
t1.m1()
t1.d=40
t2 = Test()
print(t1.__dict__)
print(t2.__dict__)