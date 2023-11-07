# Если хочу чё нить записать в файл
import os.path


def write_to_file():
    with open('СЯП_3,1/F1.txt', 'w') as file:
        print("Введите данные для записи в файл F1: ")
        while True:
            data = input()
            if not data:
                break
            file.write(data + '\n')

def copy_odd_lines():
    with open('СЯП_3,1/F1.txt', 'r') as file1, open('СЯП_3,1/F2.txt', 'w') as file2:
        lines = file1.readlines()
        odd_lines = [line for index, line in enumerate(lines) if index % 2 != 0]
        for line in odd_lines:
            file2.write(line)

def calculate_file_sizes():
    size_F1 = os.path.getsize('СЯП_3,1/F1.txt')
    size_F2 = os.path.getsize('СЯП_3,1/F2.txt')
    print(f"Размер файла F1.txt: {size_F1} байт")
    print(f"Размер файла F2.txt: {size_F2} байт")


write_to_file()
copy_odd_lines()
calculate_file_sizes()