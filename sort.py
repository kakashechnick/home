# Шейкерная сортировка
def sort(arr):
  right = len(arr) - 1  # Правый флаг (Ограничитель)
  left = 0  # Левый флаг (Ограничитель)
  logical_variable = True  # Проверка на вход

  while logical_variable:  # Пока не будет отсортирован список, цикл не закончится
    logical_variable = False  # Что бы не было бесконечного цикла, если не было входа во вложенные циклы,
    # то сортировка закончена
    minnum = left  # Начало отчета с левой стороны каждой итерации

    for item in range(left, right):  # Задаются границы с лева на право
      if arr[item] < arr[minnum]:  # Поиск наименьшего
        minnum = item  # Новое наименьшее значение
      logical_variable = True  # Проверка на вход

    arr[left], arr[minnum] = arr[minnum], arr[left]  # Обмен местами
    left += 1  # Флаг увеличивается

    maxnum = right  # Начало отчета с правой стороны каждой итерации
    for item in range(right, left - 1, -1):  # Задаются границы с права на лево
      if arr[item] > arr[maxnum]:  # Поиск наибольшего
        maxnum = item  # Новое наибольшее значение
      logical_variable = True  # Проверка на вход

    arr[right], arr[maxnum] = arr[maxnum], arr[right]  # Обмен местами
    right -= 1  # Флаг уменьшается

    print(arr)


if __name__ == '__main__':
  sort([3, 10, 7, 5, 1, 4, 9, 6, 8, 2])