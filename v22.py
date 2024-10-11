import os
from googletrans import Translator, LANGUAGES

# Ініціалізація перекладача
translator = Translator()

# Функція для перекладу тексту
def TransLate(text: str, src: str = 'auto', dest: str = 'en') -> str:
    # Перекладає текст на вказану мову або повідомляє про помилку.
    try:
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        return f"Помилка: {str(e)}"
    
def CodeLang(lang: str) -> str:
    #Повертає код мови або назву мови.
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return TransLate("Помилка: не знайдено відповідного коду мови.")

# Основна програма
def save_data_to_file(file_name, a, b, lang):
    with open(file_name, 'w') as file:
        file.write(f"{a}\n{b}\n{lang}")

def read_data_from_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 3:
                a = int(lines[0].strip())
                b = int(lines[1].strip())
                lang = lines[2].strip()
                return a, b, lang
    return None

def check_number(a, b, lang):
    sum_abs = abs(a + b)
    result = f"|{a}+{b}| = {sum_abs}\n"
    
    if sum_abs % 2 == 0:
        result += TransLate(f"{sum_abs} є парним,", dest=lang)+ " "
    else:
        result += TransLate(f"{sum_abs} не є парним, ", dest=lang) + ""
    
    if sum_abs % 10 == 7:
        result += TransLate("та закінчується цифрою 7.", dest=lang)
    else:
        result += TransLate("та не закінчується цифрою 7.", dest=lang)
    
    return result

def main():
    file_name = "MyData"

    # Спробуємо прочитати дані з файлу
    data = read_data_from_file(file_name)
    
    if data:
        a, b, lang = data
        print(TransLate(f"Мова: ", dest=lang) + CodeLang(lang))
        print(TransLate("Ціле число a: ", dest=lang) + str(a))
        print(TransLate("Ціле число b: ", dest=lang) + str(b))
    else:
        # Якщо даних у файлі немає, вводимо вручну
        try:
            lang = input("Введіть код мови (наприклад, uk для української, en для англійської): ").strip().lower()

            a = int(input(TransLate("Введіть ціле число a: ", dest=lang)))
            b = int(input(TransLate("Введіть ціле число b: ", dest=lang)))

            # Змінюємо знак від’ємних чисел
            #if a < 0:
            #    a = -a
            #if b < 0:
            #    b = -b
            
            save_data_to_file(file_name, a, b, lang)
            print(TransLate(f"Дані збережено в файл {file_name}", dest=lang))
        except ValueError:
            print(TransLate("Некоректний ввід даних.", dest=lang))
            return
    
    # Перевіряємо число
    print(check_number(a, b, lang))

if __name__ == "__main__":
    main()
