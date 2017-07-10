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
    
# Задача №1

# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца
# и номер полки, на котором он будет храниться.


def show_person():
    number = input("Введите номер документа:\n")
    for doc in documents:
        if doc["number"] == number:
            print(doc["name"])


def list_person():
    for doc in documents:
        print("{0} {1} {2}".format(doc["type"], doc["number"], doc["name"]))


def shelf():
    number = input("Введите номер документа:\n")
    for shelves, docs_on_shelf in directories.items():
        for doc in docs_on_shelf:
            if doc == number:
                print("Документ c номером {0} лежит на полке {1}".format(doc, shelves))
                break
            else:
                print('Документ не найден')


def add():
    doc_type = input("Введите тип документа: ")
    doc_number = input("Введите номер документа: ")
    doc_name = input(str("Введите имя владельца: "))
    doc_shelf = input(str("На какую полку положить документ?"))
    documents.append({"type": doc_type, "number": doc_number, "name": doc_name})
    print(documents)
    directories{"doc_shelf": doc_shelf, "number": doc_number}


#    doc_shelf = input(int("На какую полку положить документ?"))
#     documents["type"] = doc_type
#     documents["number"] = doc_number
#     documents["name"] = doc_name
#     # directories["doc_shelf"] = doc_shelf
#     directories["doc_number"] = doc_number
#     # print(directories)

# show_person()
# list_person()
# shelf()
add()
