# https://www.youtube.com/watch?v=UldZOLylez4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=73
pos = -1
lst = [2, 5, 3, 7, 9]


def search(lst, n):
    i = 0
    while i < len(lst):
        if n == lst[i]:
            global pos
            pos = i
            return True
        i = i + 1
    return False


if search(lst, 9):
    print("Found at position ", pos)
else:
    print("Not found")
