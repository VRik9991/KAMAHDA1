with open("task.txt", "r") as file:
    oskars = file.readlines()
    oskars.pop(0)
    for i in range(len(oskars)):
        pomp = oskars[i].split(",")
        oskars[i] = pomp
    # oskars = sorted(oskars, key=lambda X: X[1])
    # print(oskars[0][3])
    # print(oskars[0][4])
    for i in range(len(oskars)):  # Цыкл i = сч, лен(оскарс) = количевство елементов
        if oskars[i][3][2] == "P" and oskars[i][4][2] == "T":  # проверяем что име на Р а фильм на Т, 2 = п.б.И.и.Ф.
            print(oskars[i][3])  # Име 3 = ИМЕ
            print(oskars[i][4])  # фильм 4 = ФИЛЬМ
