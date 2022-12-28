from task1_functions import quick_sort, comb_sort
import timeit
import copy
import random

def get_shuffled_array_of_n(n):
    array = [i for i in range(n)]
    random.shuffle(array)
    return array

def get_array_from_user():
    def get_array(ustr: str):
        data = ustr.split()
        num_data = []
        for item in data:
            try:
                num_data.append(float(item))
            except:
                return [], False
        return num_data, True

    while True:
        ustr = input("Напишите числа которые нужно отсортировать через пробел:\n")
        data, valid = get_array(ustr)
        if not valid:
            print("Данные были введены не корректно")
            continue
        return data

def action_quicksort():
    data = get_array_from_user()
    data = quick_sort(data)
    print("Отсортированные данные с помощью quicksort:\n", data)

def action_combsort():
    data = get_array_from_user()
    comb_sort(data)
    print("Отсортированные данные с помощью combsort:\n", data)

arr = []

def action_compare():
    def get_n(text):
        while True:
            inpt = input(text)
            try:
                return int(inpt)
            except:
                pass
    n = get_n("Напишите число элементов для теста: ")
    n_repeats = get_n("Напишите кол-во повторений: ")
    global arr
    arr = get_shuffled_array_of_n(n)
    print("Начало quicksort")
    quicksort_time = timeit.timeit("quick_sort(carr)", setup="carr = copy.deepcopy(arr)", number=n_repeats, globals=globals())
    print("Конец quicksort\nНачало combsort")
    combsort_time = timeit.timeit("comb_sort(carr)",  setup="carr = copy.deepcopy(arr)", number=n_repeats, globals=globals())
    print("Конец combsort")
    print(f"\nВремя сортировки quicksort: {quicksort_time}\n"
          f"Время выполнения combsort: {combsort_time}")

if __name__ == "__main__":
    while True:
        inpt = input("Отсортировать массив быстрой сортировкой - 1\n"
                     "Отсортировать массив сортировкой расчесткой - 2\n"
                     "Сравнить сортировки - 3\n")
        if inpt not in ["1", "2", "3"]:
            continue
        if inpt == "1":
            action_quicksort()
            break
        if inpt == "2":
            action_combsort()
            break
        if inpt == "3":
            action_compare()
            break