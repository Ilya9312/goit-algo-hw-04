def parse_input(user_input): #робимо функцію обробки команд
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts): #ця функція додає контакт в словник
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."


def change_contact(args, contacts): #ця функція змінює контакт в словнику
    name, new_phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = new_phone
        return 'Contact updated'
    else:
        return 'Contact not found'




def show_contact(args, contacts): #ця функція показує контакт певної людини за її ім'ям
    name = args[0]
    name = name.lower() #тут зробив цю функцію нечутливою до регістру,у функції зміни номера, також зробив це
    if name in contacts:
        phone = contacts[name]
        return f'Person number is: {phone}'
    else:
        return 'Контакт не знайдено'


def show_all(args, contacts): #ця функція показує всю інформацію про користувачів які збережені у словник контакти,тобто ім'я та номер
    for name, phone in args:
        contacts[name.lower()] = phone

    return contacts

#основна функція нашого в якій зберігаються дані та в якій оброблюються всі дії,які хоче зробити користувач зі своїм списком контактів
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        # прописуємо логіку реагування на команди
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
