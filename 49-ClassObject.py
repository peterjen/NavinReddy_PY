class Computer:
    cpu = ""
    ram = ""

    def __init__(self, c, r):
        self.cpu = c
        self.ram = r

    def config(self):
        print(self.cpu, self.ram, "1TB")


a = Computer("i5", "16")
# print(type(a))
a.config()
b = Computer("R5", "32")
b.config()


class Car:
    wheels = 4

    def __init__(self):
        self.company = 'BMW'
        self.mil = 10


c1 = Car()
c2 = Car()
c1.wheels = 5  # INSTANCE VARIABLE
print(c1.company, c1.mil, c1.wheels)
print(c2.company, c2.mil, c2.wheels)

Car.wheels = 5  # CLASS VARIABLE
print(c1.company, c1.mil, c1.wheels)
print(c2.company, c2.mil, c2.wheels)


# https://www.youtube.com/watch?v=lVfGQOzzRCM&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=57

class Student:
    school = 'ABC'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  #### instant method
        return (self.m1 + self.m2 + self.m3) / 3

   @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod  # Nothing related to instant VAR and class VAR, NO (self) or (cls)
    def info():
        print('This is Student class..............')


s1 = Student(12, 23, 34)
s2 = Student(45, 56, 67)

print(s2.avg())

print(s2.get_school())
print(Student.get_school())

Student.info()
s1.info()
