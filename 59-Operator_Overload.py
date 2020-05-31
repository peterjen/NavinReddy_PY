class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # OPERATOR OVERLOADING : +
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        obj = Student(m1, m2)
        return obj

    def __eq__(self, other):  # OPERATOR OVERLOADING : ==
        if self.m1 == other.m1 and s1.m2 == other.m2:
            return True
        return False

    def __gt__(self, other):  # OPERATOR OVERLOADING : >
        if self.m1 + self.m2 > other.m1 + other.m2:
            return True
        return False

    def __str__(self):
        string = '{} {} '.format(self.m1, self.m2)
        return string
        # return str(self.m1) + " " + str(self.m2)


s1 = Student(21, 23)
s2 = Student(34, 43)
s3 = s1 + s2
print(s3.m1, s3.m2)
print(s1 == s2)
print(s1 > s2)

print(s1)
