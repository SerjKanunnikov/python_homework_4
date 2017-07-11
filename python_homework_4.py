documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def show_person():
    number = input("Введите номер документа:\n")
    for doc in documents:
        if doc["number"] == number:
            print(doc["name"])


def list_person():
    for doc in documents:
        print("{0} {1} {2}".format(doc["type"], doc["number"], doc["name"]))


def find_shelf():
    number = input("Введите номер документа:\n")
    for shelves, docs_on_shelf in directories.items():
        for doc in docs_on_shelf:
            if doc == number:
                print("Документ c номером {0} лежит на полке {1}".format(doc, shelves))
                break


def add():
    doc_type = input("Введите тип документа: ")
    doc_number = input("Введите номер документа для удаления: ")
    doc_name = input(str("Введите имя владельца: "))
    doc_shelf = input(str("На какую полку положить документ? "))
    documents.append({"type": doc_type, "number": doc_number, "name": doc_name})
    directories[doc_shelf].append(doc_number)
    print(documents)
    print(directories)


def delete():
    number = input("Введите номер документа для удаления: ")
    for doc in documents:
        if doc["number"] == number:
            documents.remove(doc)
            print(documents)


def move():
    number = input("Введите номер документа для перемещения: \n")
    new_shelf = input("Укажите полку, на которую нужно переместить документ: \n")
    for shelves, docs_on_shelf in directories.items():
        for doc in docs_on_shelf:
            if doc == number:
                docs_on_shelf.remove(doc)
                directories[new_shelf].append(doc)
    print(directories)


def add_shelf():
    shelf_name = input("Введите номер новой полки: \n")
    directories[shelf_name] = []
    print(directories)


def choose_command():
    while True:
        command = input("Введите команду: \n"
              "p — вывести имя владельца по номеру документа\n"
              "l — вывести список всех документов\n"
              "s — найти полку по номеру документа\n"
              "a — добавить новый документ\n"
              "d — удалить документа по его номеру\n"
              "m — переместить документ на другую полку\n"
              "as — создать новую полку\n")
        if command == "p":
            show_person()
        elif command == "l":
            list_person()
        elif command == "s":
            find_shelf()
        elif command == "a":
            add()
        elif command == "d":
            delete()
        elif command == "m":
            move()
        elif command == "as":
            add_shelf()
        else:
            print("Введите правильную команду")

choose_command()
