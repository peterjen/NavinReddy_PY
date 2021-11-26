# https://www.youtube.com/watch?v=DE-ye0t0oxE&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=74


def search(lst, n):
    l = 0
    u = len(lst) - 1

    fnd = False
    search_num = 8

    # while fnd == False:
    while l <= u:
        # print(l, u)
        m = int((l + u) / 2)
        if n == lst[m]:
            fnd = True
            print("FOUND ", n, " at ", m)
            return True
        elif n > lst[m]:
            l = m + 1
        else:
            u = m - 1
    return False


lst = [4, 7, 8, 12, 45, 99]
if search(lst, 999):
    print("FOUND")
else:
    print("NOT FOUND")
