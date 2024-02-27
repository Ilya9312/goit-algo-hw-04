def get_cats_info(path):
    # обробляю виняток за допомогою обробника try,except
    try:
        with (open(path, 'r+', encoding='utf-8') as fh):  # за допомогою менеджера контексту відкриваю файл з котами
            cats_info = []  # записую сюди сформованний список словників з котами
            # прохожусь циклом по усім котам,та додаю у список cats_info словники з котами по айді та за ім'ям і віком,розділюючи їх по комі
            for cats in fh:
                cat_id, name, age = cats.strip().split(',')
                cats_info += ([{"id": cat_id, "name": name, "age": age, }])
            return cats_info  # повертаю відсортованний список словників за вказанними в задачі потребами

    # оброблюю виняток,якщо вайл не знайдено
    except FileNotFoundError:
        print('File not found')
        return None
    # Оброблюю усі винятки,та зазначаю їх як помилку в обробці файлу
    except Exception as e:
        print('Помилка при обробці файлу')
        return None


# викликаю та виводжу результат функції з готовою інформацією про котів
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
