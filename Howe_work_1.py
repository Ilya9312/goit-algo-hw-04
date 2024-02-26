def total_salary(path):
    # обробляю виняток за допомогою обробника try,except
    try:
        with open(path, 'r+', encoding='utf-8') as fh:
            total_sum = 0  # зазначаю лічильник для суми усіх зарплат разом
            worker_count = 0  # лічильник для кількості працівників
            # цикл для виведення усіх зарплат та розрахунку середньої зарплати
            for salary in fh:
                workers, salary = salary.strip().split(',')
                total_sum += int(salary)  # розраховую загальну зарплатню усіх робітників
                worker_count += 1  # кожну ітерацію додаю до працівників 1,щоб порахувати їх кількість
                mid_salary = total_sum // worker_count  # розраховую середню зарплатню
            return total_sum, mid_salary  # повертаю кортеж з зарплатами,загальну та середню

    # оброблюю виняток,якщо вайл не знайдено
    except FileNotFoundError:
        print('File not found')
        return None
    # Оброблюю усі винятки,та зазначаю їх як помилку в обробці файлу
    except Exception as e:
        print('Помилка при обробці файлу')
        return None
    
    
# оброблюю сирі дані визиваючи функцію total_salary та виводжу на экран оброблені дані завдяки цій функції
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
