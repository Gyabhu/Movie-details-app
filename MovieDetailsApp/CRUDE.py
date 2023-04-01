from create import create
from read import read
from update import update
from delete import delete
from passCreator import ask_pwd


def ask():
    selected = input("Welcome to Gab's Fort, Choose C/R/U/D/E/P: ")
    selected.lower()

    def continue_or_not(c):
        ask() if c else print("May the fort be with you! Bye.")

    if selected == 'c':
        cont = create()
        return continue_or_not(cont)
    elif selected == 'r':
        id = int(input("Enter your id: "))
        cont = read(id)
        return continue_or_not(cont)

    elif selected == 'u':
        id = int(input("Enter your id: "))
        key = input("Select info for update,(Name,Movies): ")
        value = input("Enter your info for update: ")
        cont = update(id, key, value)
        return continue_or_not(cont)

    elif selected == 'd':
        id = int(input("Enter the id you want to delete: "))
        cont = delete(id)
        return continue_or_not(cont)

    elif selected == 'p':
        password = input("Set New Pass: ")
        id = input("Id for Password: ")
        cont = ask_pwd(password, id)
        return continue_or_not(cont)

    elif selected == 'e':
        print("May the fort be with you! Bye.")

    else:
        print("Choose the correct keyword!")
        ask()


ask()