# %%
class Student:
    ''' This class is developed by durga for demo'''
    # variables
    # methods

print(Student.__doc__)
help(Student)

# %%
class student:
    ''' Class developed by durga for demp'''
    def __init__(self):
        self.name = 'Durga'
        self.rollno = 101
        self.marks = 90
    def talk(self):
        print("Hello I am:",self.name)
        print("My roll no is: ",self.rollno)
        print("My marks are: ",self.marks)

# %%
s1 = student()

# %%
s1.talk()

# %%
class student:
    ''' Class developed by durga for demp'''
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print("Hello I am:",self.name)
        print("My roll no is: ",self.rollno)
        print("My marks are: ",self.marks)

# %%
s2 = student("saikiran",102,99)

# %%
s2.talk()

# %%
class Test:
    def __init__(self):
        pass
    

# %%
t = Test()
print("Adress of object pointed by t:",id
(t))

# %%
class Test:
    def m1(self):
        print("method")

# %%
t1 = Test()
t1.m1()

# %%
## Constructor is not mandatory in python where python provides defalut constructor


# %%
class Test:
    def __init__(self):
        print('constructor execution')
        

# %%
k = Test()
k.__init__()
k.__init__()
k.__init__()
k.__init__()
k.__init__()

# %%
class Movie:
    '''This class developed by durga for demo purpose'''
    def __init__(self,title,hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine
    
    def info(self):
        print('Moive name: ',self.title)
        print('Hero name: ',self.hero)
        print('Heroine name: ',self.heroine)
list_of_movies = []
while True:
    title = input("Enter the movie name: ")
    hero = input("Enter hero name: ")
    heroine = input("Enter heroine name: ")
    m = Movie(title,hero,heroine)
    list_of_movies.append(m)
    print("Moive added successfully....")
    option = input('Do you want to addd one more moive [yes/no]:')
    if option.lower()=='no':
        break


# %%
class Add:

    def Add(self):
        a = 10
        b = 20
        print('a+b:',self.a+self.b)

# %%
A1 = add()

# %%
A1 = Add()

# %%
A1.Add()

# %%
class Add:

    def Add(self):
        self.a = 10
        self.b = 20
        print('a+b:',self.a+self.b)

# %%
A1 = Add()-

# %%
A1 = Add()-

# %%
A1 = Add()

# %%
A1.Add()

# %%
class Add:

    def Add(self):
        self.a = 10
        self.b = 20
        print('a+b:',a+b)

A1 = Add()
A1.Add()

# %%
class Add:

    def Add(self):
        self.a = 10
        self.b = 20
        print('a+b:',self.a+self.b)

A1 = Add()
A1.Add()

# %%
class Student:
    schoolname = "Durga soft"  #--------------------> Static variables

    def __init__(self,name,rollno):
        self.name = name          #------------------> Instance variables
        self.rollno = rollno      #------------------> Instance variables

    def get_student_info(self):   #-------------------> Instance method
        print("Student name: ",self.name)
        print("Student rolllno: ",self.rollno)

s1 = Student('Jhonny',101)
s1.get_student_info()

# %%
class Student:
    schoolname = "Durga soft"  #--------------------> Static variables

    def __init__(self,name,rollno):
        self.name = name          #------------------> Instance variables
        self.rollno = rollno      #------------------> Instance variables

    def get_student_info(self):   #-------------------> Instance method
        print("Student name: ",self.name)
        print("Student rolllno: ",self.rollno)
        print("School name: ",Student.schoolname)

s1 = Student('Jhonny',101)
s1.get_student_info()

# %%
class Student:
    schoolname = "Durga soft"  #--------------------> Static variables

    def __init__(self,name,rollno):
        self.name = name          #------------------> Instance variables
        self.rollno = rollno      #------------------> Instance variables

    def get_student_info(self):   #-------------------> Instance method
        print("Student name: ",self.name)
        print("Student rolllno: ",self.rollno)
    def get_student_school(self):
        print("Student school: ",Student.schoolname)

s1 = Student('Jhonny',101)
s1.get_student_info()
s1.get_student_school()

# %%
class Student:
    schoolname = "Durga soft"  #--------------------> Static variables

    def __init__(self,name,rollno):
        self.name = name          #------------------> Instance variables
        self.rollno = rollno      #------------------> Instance variables

    def get_student_info(self):   #-------------------> Instance method
        print("Student name: ",self.name)
        print("Student rolllno: ",self.rollno)
    @classmethod
    def get_student_school(cls):
        print("Student school: ",Student.schoolname) #-----------------> Class method

s1 = Student('Jhonny',101)
s1.get_student_info()
s1.get_student_school()

# %%
class Student:
    schoolname = "Durga soft"  #--------------------> Static variables

    def __init__(self,name,rollno):
        self.name = name          #------------------> Instance variables
        self.rollno = rollno      #------------------> Instance variables

    def get_student_info(self):   #-------------------> Instance method
        print("Student name: ",self.name)
        print("Student rolllno: ",self.rollno)
    @classmethod
    def get_student_school(cls):
        print("Student school: ",Student.schoolname)
    @staticmethod
    def get_total_marks(a,b,c,d):
        return a+b+c+d

s1 = Student('Jhonny',101)
s1.get_student_info()
s1.get_student_school()
s1.get_total_marks(20,30,40,50)


