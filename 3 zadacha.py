# ывести все пары актёров сумма возрастов которых равна 100, на пример 45 + 65
with open("task.txt", "r") as file:
    oskars = file.readlines()
    oskars.pop(0)
    for i in range(len(oskars)):
        pomp = oskars[i].split(",")
        oskars[i] = pomp
    for i in range(len(oskars)):
        oskar = oskars[i]
        for j in range(len(oskars)):
            if int(oskar[2]) + int(oskars[j][2]) == 100:
                print(f"{oskar[3]}({oskar[2]}), {oskars[j][3]}({oskars[j][2]})")
