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
