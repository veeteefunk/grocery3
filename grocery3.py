list = []

while True:
    try:
        fruit = input("")
        list.append(fruit)
        times = list.count(fruit)
        fruit_times = {fruit, times}
    except EOFError:
        print(list)
        print(fruit_times)
        break
    else:
        try:
            if fruit in list:
                {fruit : times + 1}
            else:
                fruit_times.update({fruit : times})
        except KeyError:
            pass