import csv
import sys
import os


def csv_reader(csv_path):
    with open(csv_path, "r", encoding="utf-8") as f_obj:
        reader = csv.reader(f_obj)
        try:
            for row in reader:
                yield row
        except UnicodeDecodeError:
            exit("Невозможно открыть файл")


def is_not_fired(data):
    for employee in data:
        if employee[-1] == '1':
            yield employee


def is_high_education(data):
    for employee in data:
        if employee[2] == '1':
            yield employee


def get_employeers_with_good_skills(data):
    average_skill = 90
    for employee in data:
        if float(employee[-2]) > average_skill:
            yield employee


def print_not_recommend_to_dismiss(data):
    for empolyee in data:
        print("Не рекомендуется увольнять: ", empolyee[1])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    else:
        exit("Файл не выбран. Выберите файл")
    if not(os.path.exists(csv_path)):
        exit("Файла нет в директории")
    data = csv_reader(csv_path)
    isnt_fired = is_not_fired(data)
    high_educated = is_high_education(isnt_fired)
    skilled_employees = get_employeers_with_good_skills(high_educated)
    print_not_recommend_to_dismiss(skilled_employees)
