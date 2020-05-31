# https://www.youtube.com/watch?v=UDmJGvM-OUw&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=65

from abc import ABC, abstractclassmethod

class Computer:
    @abstractclassmethod
    def process(self):  # This method only declaration but NO definition called Abstract Method
        pass

#######   SO SO SO SO SO  CONFUSING...............
c1 = Computer()
c1.process()
print(id(c1))
