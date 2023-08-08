import re


def extract_names_from_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()

    # Регулярное выражение для поиска имен в тегах <li>
    pattern = r'<li[^>]*>(.*?)<\/li'

    # Используем findall для нахождения всех совпадений регулярного выражения в строке
    matches = re.findall(pattern, data, re.DOTALL)

    # Очищаем имена от лишних пробелов и возвращаем список имен
    names = [match.strip() for match in matches]

    return names


file_path = "FPT_list.txt"


with open("fpt_num_name.txt", "a") as file:
    names_list = extract_names_from_file(file_path)

    for index, name in enumerate(names_list, 1):
        file.write(f"{index}: {name}\n")




