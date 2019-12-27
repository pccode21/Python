class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self,course_name):
        print('%s正在学习%s.'%(self.name,course_name))
    def watch_movie(self):
        if self.age<18:
            print('%s只能观看《熊出没》.'% self.name)
        else:
            print('%s正在观看岛国爱情电影.'% self.name)
            
def main():
    stu1=Student('小李',28)
    stu1.study('Python编程')
    stu1.watch_movie()
    stu2=Student('小王',16)
    stu2.study('思想品德')
    stu2.watch_movie()
    
if __name__=='__main__':
    main()