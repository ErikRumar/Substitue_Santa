
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



def menu():
    choice = -1
    while choice < 1 or choice > 3:
        print("""
                Meny
        
        1. Skapa önskelista
        2. Läs önskelista


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
            print("returned")
menu()