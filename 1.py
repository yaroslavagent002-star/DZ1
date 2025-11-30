#class Student:
 #   count = 0

  #  def __init__(self, height, name='Вася'):
   #     self.name = name
    #    self.height = height
     #  Student.count += 1

    #def info(self):
     #   print("Ріст студента:", self.height)




#st1 = Student(155)
#st2 = Student(name='Давид', height=158)
#st3 = Student(name='Саша', height=162)

#print('#', Student.count)

#print(st1.height)
#print(st2.height)
#print(st3.height)
#
#print("Всього студентів:", Student.count)
#print("ім'я студентів")
#print("Ріст студентів:")
#st1.info()
#st2.info()
#st3.info()
class Animals:      # шаблон (клас)
    count = 0

    def __init__(self, name='Кіт, Вік:', height=3):   # вбудований метод (конструктор)
        self.name = name
        self.height = height
        Animals.count += 1

    def info(self):
        print(self.name, self.height)


st1 = Animals()             # об'єкт
st2 = Animals(name='Собака, Вік:', height=5)
st3 = Animals(name='Черепаха, Вік:', height=1)


st1.info()
st2.info()
st3.info()

print('Всього тварин:', Animals.count)
