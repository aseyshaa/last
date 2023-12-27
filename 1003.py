import random
import string


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

'''Применение zip для параллельного обхода текста и ключа, а затем использование
/генератора списков для более компактного и эффективного шифрования текста.
/ (Использование zip и генератора списков для шифрования:)'''
def vigenere_cipher(text, key):
    encrypted_text = ""
    key_length = len(key)
    key = key * (len(text)//len(key)) + key[:len(text)%len(key)]  # repeat the key to match the length of the text
    encrypted_text = ''.join(chr((ord(t) - ord('a') + ord(k) - ord('a')) % 26 + ord('a')
                     if t.islower() else (ord(t) - ord('A') + ord(k) - ord('a')) % 26 + ord('A')
                     if t.isupper() else ord(t)) for t, k in zip(text, key))
    return encrypted_text
'''Также в функции выше представлено
/использование условий и циклов для управления выполнением программы'''



'''Изменила имена переменных и функций,
/чтобы отражать их функцию и назначение, что делает код более понятным'''
def input_data_manually():
    text = input("Введите текст: ")
    key = input("Введите ключ: ")
    return text, key


def input_data_random():
    text_length = random.randint(10, 20)
    key_length = random.randint(1, 5)
    text = generate_random_string(text_length)
    key = generate_random_string(key_length)
    return text, key

'''Перенесли меню в отдельную функцию, для организации кода'''
def main_menu():
    print("Меню:")
    print("1. Ввести исходные данные вручную")
    print("2. Сгенерировать случайные исходные данные")
    print("3. Выполнить алгоритм")
    print("4. Вывести результат")
    print("5. Завершить работу")


def main():
    text = ""
    key = ""
    encrypted_text = ""
    while True:
        main_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            text, key = input_data_manually()
            encrypted_text = "" 
        elif choice == "2":
            text, key = input_data_random()
            print("Выбранный текст - " + text)
            print("Выбранный ключ - " + key)
            encrypted_text = ""  
            ''' Использование метода filter для удаления всех символов, не являющихся/
                буквами, из введенного текста до его шифрования. (Предварительная обработка текста:)'''
        elif choice == "3":
            if text and key:
                text = ''.join(filter(str.isalpha, text))  
                encrypted_text = vigenere_cipher(text, key)
                print("Алгоритм выполнен.")
            else:
                print("Введите исходные данные перед выполнением алгоритма.")
        elif choice == "4":
            if encrypted_text:
                print("Зашифрованный текст: " + encrypted_text)
            else:
                print("Результаты алгоритма не получены.")
        elif choice == "5":
            break
        else:
            print("Неверный выбор пункта меню. Попробуйте ещё раз.")


if __name__ == "main":
    main()
