from Aliment import ali
from Aliment import datum
import sys
import time
import datetime
import sys
import curses
from curses import wrapper



def ajouter():



 while True:
    toutp = (input("\nVoulez vous continuer?(oui ou non):"))
    if toutp == "oui" or toutp == "Oui":
        ram = (input("Vous voulez ajouter quoi?:"))
        date = (input("date de l'aliment ex21/10/14:"))
        cav = f"{ram} "
        vac = f"{date}"

        ali.extend([cav])
        datum.extend([vac])

        new = f"ali = {ali}\n"
        dat = f"\ndatum= {datum}"

        print(new)
        print(dat)

        with open("Aliment.py", "w") as file:
                file.write(new)
                file.write(dat)
                file.close()

    if toutp== "non" or toutp =="Non":

        quit()


def verifier():
    target = (input("Scanner:"))

    found = False

    for element in ali:
        if element == target:
            print(f'elément trouver {element}')
            # z = zip(ali, datum)
            # print(list(z))
            print(ali)
            break

    else:
        print(f"élement non trouver ")

def voir():
    while True:
        Numbelem = len(datum)
        print(Numbelem)
        # si le nombre d'element est de 3
        if Numbelem == 1:
            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[0]

            formatted_datenow = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow:
                print(f"\n{ali[0]} est perimé le {datum[0]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow:
                print(f"\n{ali[0]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[0])
                datum.remove(datum[0])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()

            else:
                exit()

        # si le nombre en elements est  de 2
        if Numbelem == 2:
            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[0]

            formatted_datenow = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow:
                print(f"\n{ali[0]} est perimé le {datum[0]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow:
                print(f"\n{ali[0]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[0])
                datum.remove(datum[0])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()

            else:
                exit()

            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[1]

            formatted_datenow1 = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow1:
                print(f"\n{ali[1]} est perimé le {datum[1]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow1:
                print(f"\n{ali[1]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[1])
                datum.remove(datum[1])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()

            else:
                exit()

        if Numbelem == 3:
            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[0]

            formatted_datenow = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow:
                print(f"\n{ali[0]} est perimé le {datum[0]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow:
                print(f"\n{ali[0]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[0])
                datum.remove(datum[0])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()
            else:
                exit()

            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[1]

            formatted_datenow1 = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow1:
                print(f"\n{ali[1]} est perimé le {datum[1]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow:
                print(f"\n{ali[1]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[1])
                datum.remove(datum[1])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()

            else:
                exit()

            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[2]

            formatted_datenow1 = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow1:
                print(f"\n{ali[2]} est perimé le {datum[2]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow:
                print(f"\n{ali[2]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[2])
                datum.remove(datum[2])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()
            else:
                exit()

        if Numbelem == 4:
            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[0]

            formatted_datenow = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow:
                print(f"\n{ali[0]} est perimé le {datum[0]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow:
                print(f"\n{ali[0]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[0])
                datum.remove(datum[0])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()

            else:
                exit()

            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[1]

            formatted_datenow1 = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow1:
                print(f"\n{ali[1]} est perimé le {datum[1]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow:
                print(f"\n{ali[1]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[1])
                datum.remove(datum[1])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()
            else:
                exit()

            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[2]
            print(datum[2])

            formatted_datenow2 = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow2:
                print(f"\n{ali[2]} est perimé le {datum[2]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow2:
                print(f"\n{ali[2]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[2])
                datum.remove(datum[2])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()

            else:
                exit()

            now = datetime.datetime.now()
            datenow = (now.strftime("%d/%m/%y"))
            dateduj = datenow
            date = datum[3]

            formatted_datenow3 = time.strptime(dateduj, "%d/%m/%y")
            formatted_date = time.strptime(date, "%d/%m/%y")

            if formatted_date < formatted_datenow3:
                print(f"\n{ali[3]} est perimé le {datum[3]} nous sommes le: {dateduj}")
            if formatted_date == formatted_datenow3:
                print(f"\n{ali[3]} est perimé aujourd'hui le: {dateduj}")

            supp = input(f"Voulez vous supprimer cet aliment?:")
            if supp == "oui" or supp == "Oui":
                ali.remove(ali[3])
                datum.remove(datum[3])

                rm = f"ali = {ali}\n"
                mr = f"datum = {datum}"

                print(rm)
                print(mr)

                with open("Aliment.py", "w") as file:
                    file.write(rm)
                    file.write(mr)
                    file.close()

            else:
                exit()


def numa1():
    now = datetime.datetime.now()
    datenow = (now.strftime("%d/%m/%y"))
    dateduj = datenow
    date = datum[0]
    print(datum[0])

    formatted_datenow = time.strptime(dateduj, "%d/%m/%y")
    formatted_date = time.strptime(date, "%d/%m/%y")

    if formatted_date < formatted_datenow:
        print(f"\n{ali[0]} est perimé le {datum[0]} nous sommes le: {dateduj}")
    if formatted_date == formatted_datenow:
        print(f"\n{ali[0]} est perimé aujourd'hui le: {dateduj}")

    supp = input(f"Voulez vous supprimer cet aliment?:")
    if supp == "oui" or supp == "Oui":
        ali.remove(ali[0])
        datum.remove(datum[0])

        rm = f"ali = {ali}\n"
        mr = f"datum = {datum}"

        print(rm)
        print(mr)

        with open("Aliment.py", "w") as file:
            file.write(rm)
            file.write(mr)
            file.close()

def aff(stdscr):
    curses.init_pair(1, curses.COLOR_RED,curses.COLOR_WHITE)
    ORANGE_AND_WHITE = curses.color_pair(1)

    stdscr.clear()
    stdscr.addstr(5, 10, "+++++++++++++++++++++++++++++++++++++++++++++++",ORANGE_AND_WHITE)
    stdscr.addstr(6, 10, "++                FRIGOT                     ++",ORANGE_AND_WHITE)
    stdscr.addstr(7, 10, "+++++++++++++++++++++++++++++++++++++++++++++++",ORANGE_AND_WHITE)
    stdscr.addstr(8, 10, "++            Made By Dylan Briancourt       ++",ORANGE_AND_WHITE)
    stdscr.addstr(9, 10, "+++++++++++++++++++++++++++++++++++++++++++++++",ORANGE_AND_WHITE)
    stdscr.refresh()
    stdscr.getch()

wrapper(aff)

print(f'            \n      +++++++++++++++++++++++++++++++++++++++++++++++')
print(f'      ++                FRIGOT                     ++')
print(f'      +++++++++++++++++++++++++++++++++++++++++++++++\n')




toutp = input("     Ajouter // Verifier // voir // analyser lefrigo: ")

while True:
    #action to add elements on my list
    if toutp == "Ajouter" or toutp == "ajouter":
          ajouter()


    if toutp == "Verifier" or toutp == "verifier":
            verifier()




    if toutp == "voir" or toutp =="Voir":
        voir()




    if toutp =="analyser":
        z = zip(ali,datum)
        print(list(z))
        break