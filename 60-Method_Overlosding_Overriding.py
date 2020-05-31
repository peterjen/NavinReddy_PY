print("\n### OVERLOADING")

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sumall(self, *args):
        s = 0
        for i in args:
            s = s + i
        return s


s1 = Student(22, 33)
print(s1.sumall(2, 3))
print(s1.sumall(2, 3, 4, 2, 3, 4, 5, ))


print("\n### OVERRIDING")

class A:
    def show(self):
        print("in A show...")
class B(A):
    def show(self):
        print("in B show...")

a1 = A()
a1.show()
a2 = B()
a2.show()