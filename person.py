class Person(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @name.setter
    def name(self,name):
        self._name=name   
    @age.setter
    def age(self,age):
        self._age=age   
    def play(self):
        if self._age<=16:
            print('%s正在玩飞机棋.'%self._name)
        else:
            print('%s正在玩斗地主.'%self._name)
class Student(Person):
    def __init__(self,name,age,grade):  #子类Student继承父类提供的属性name,age
        super().__init__(name,age)      #子类Student定义自己特有的属性grade
        self._grage=grade
    @property
    def grade(self):                    #子类Student定义自己特有的方法grade
        return self._grade
    @grade.setter
    def grade(self,grade):
        self._grage=grade
    def study(self,course):             #子类Student定义自己特有的方法study
        print('%s的%s正在学习%s'%(self._grage,self._name,course))
class Teacher(Person):
    def __init__(self,name,age,title):
        super().__init__(name,age)    #子类Tercher继承父类提供的属性name,age
        self._title=title             #子类Tercher定义自己特有的属性title
    @property
    def title(self):                  #子类Tercher定义自己特有的方法title
        return self._title
    @title.setter
    def title(self,title):
        self._title=title
    def teach(self,course):           #子类Tercher定义自己特有的方法teach
        print('%s%s正在讲%s'%(self._name,self._title,course))
def main():
    #person=Person('小王',18)
    stu=Student('小林',15,'初二')
    stu.study('数学')
    stu.play()                        #子类Student继承父类提供的方法play
    #person.name='小李'
    #person.age=12
    t=Teacher('王老师',38,'特级教师')
    t.teach('物理')     
    t.play()                          ##子类Teacher继承父类提供的方法play
if __name__=='__main__':
    main()