import time

global choice

def create():
    global choice

    name = input("namn på önskelista: ")
    owner = input("Vem äger den: ")
    amount = int(input("How many wishes: "))
    with open(f"{name}.txt", "w", encoding="utf8") as lista:
        lista.write(owner)
        lista.write("\n")
        lista.write(name)
        lista.write("\n")
        for x in range(amount):
            print(x+1, end= ": ")
            add = input("")
            if x < amount:
                lista.write(add)
                lista.write("\n")
            else:
                lista.write(add)
    choice = -1


def read():
    global choice

    file = input("Vad heter önskelistan? ")
    with open(f"{file}.txt", "r", encoding= "utf8") as lista:
        owner = lista.readline()
        name = lista.readline()
        print(owner)
        print(name)
        lin = 0
        for x in lista.readlines():
            lin += 1
            print(lin, x)
    choice = -1


def createn():
    global choice
    amount = int(input("How many naughty children: "))
    with open(f"naughtychildrenlist.txt", "r", encoding="utf8") as listas:
        listn = listas.readlines()
    with open(f"naughtychildrenlist.txt", "w", encoding="utf8") as lista:
        for x in range(amount):
            print(x+1, end= ": ")
            add = input("")
            if x < amount:
                listn.append(add)
                listn.append("\n")
            else:
                listn.append(add)
        for y in listn:
            lista.write(y)
    choice = -1


def readn():
    global choice
    with open(f"naughtychildrenlist.txt", "r", encoding= "utf8") as lista:
        time.sleep(0.5)
        print("Naughtlist:\n")
        time.sleep(1)
        lin = 0
        for x in lista.readlines():
            lin += 1
            print(lin, x)
    choice = -1



def menu():
    choice = -1
    while choice < 1 or choice > 5:
        print("""
                Meny
        
        1. Skapa önskelista
        2. Läs önskelista
        3. Skapa ny naughty list
        4. Lägg till på naughty list
        5. Läs naughty list


        """)
        choice = int(input("Val: "))
        if choice == 1:
            create()
            choice = -1
        if choice == 2:
            read()
            choice = -1
        if choice == 3:
            with open(f"naughtychildrenlist.txt", "w", encoding="utf8") as listaszn:
                listaszn.write("")
            createn()
            choice = -1
        if choice == 4:
            createn()
            choice = -1
        if choice == 5:
            readn()
            choice = -1
        if choice == 3:
            break
        else:
            time.sleep(0.5)
            print("returned")
            time.sleep(1)
menu()