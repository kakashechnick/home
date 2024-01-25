# Шейкерная сортировка
def sortShake(arr):
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


# Пирамидальная сортировка
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1   # left = 2*i + 1
    right = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if left < n and arr[i] < arr[left]:
        largest = left

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if right < n and arr[largest] < arr[right]:
        largest = right

    # Заменяем корень, если нужно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера


def heapSort(arr):
  num = len(arr)

  # Построение max-heap.
  for item in range(num, -1, -1):
      heapify(arr, num, item)

  # Один за другим извлекаем элементы
  for item in range(num-1, 0, -1):
      arr[item], arr[0] = arr[0], arr[item]  # свап
      heapify(arr, item, 0)
      print(arr)


if __name__ == '__main__':
  sortShake([3, 10, 7, 5, 1, 4, 9, 6, 8, 2])
  print()
  arr = [3, 10, 7, 5, 1, 4, 9, 6, 8, 2]
  heapSort(arr)

