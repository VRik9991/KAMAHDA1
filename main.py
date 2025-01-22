with open("task.txt", "r") as file:
    oskars = file.readlines()
    oskars.pop(0)
    for i in range(len(oskars)):
        pomp = oskars[i].split(",")
        oskars[i] = pomp
    oskars = sorted(oskars, key=lambda X: X[1])
    print(oskars[0][3])
    print(oskars[0][4])