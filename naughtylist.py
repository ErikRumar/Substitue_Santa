import time


global choice

def create():
    global choice
    amount = int(input("How many naughty children: "))
    with open(f"naughtychildrenlist.txt", "w", encoding="utf8") as lista:
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
    while choice < 1 or choice > 3:
        print("""
                Meny
        
        1. Skapa naughty list
        2. Läs naughty list


        """)
        choice = int(input("Val: "))
        if choice == 1:
            create()
            choice = -1
        if choice == 2:
            read()
            choice = -1
        if choice == 3:
            break
        else:
            time.sleep(1)
            print("returned")
menu()