a = ["Вячеслав", "Андрюша", "Стас", "Алексей",
     "Андрюша", "Вика", "Максим", "Андрюша",
     "Даня", "Андрюша"]


def escape_andrey_from_military(a, item):
    for i in range(a.count(item)):
        a.remove(item)
    return a


print(a)
a = escape_andrey_from_military(a, "Андрюша")
print(a)
