# Дан одномерный целочисленный массив порядка N.
# Найдите сумму отрицательных элементов массива,
# стоящих между первым и последним положительными
# элементами. Если таких элементов нет, вернуть значение 0.


def positive_number_between_negative(lens):
  import random as rnd

  array = []
  for item in range(lens):  # Заполнение списка
    array.append(rnd.randint(-10, 10))

  print(array)

  iterator = int()
  if array[0] > 0 and array[len(array) - 1] > 0:  # Проверка первого и последнего элемента списка
    for item in array:  # Проход по каждому из элементов
      if item < 0:  # Отрицательное или положительное
        iterator += item
    return iterator

  else:
    return 0


# Самая длинная строка в массиве вводятся строки.
# Определить самую длинную строку и вывести ее номер на экран.
# Если самых длинных строк несколько, то вывести номера всех таких строк.


def comparison_of_lengths(arr: list):
  maxlen = arr[0]  # Наибольший элемент всегда первый по списку

  print(arr)

  for item in arr:  # Итеравция по каждому элементу списка
    if len(item) > len(maxlen):  # Если он больше начального, то он и становиться новым наибольшим
      maxlen = item

  start = int()
  for item in arr:  # Окончательный проход
    if len(item) == len(maxlen):  # Если в списке есть объект такой же по длине как и наибольший, то
      print(arr.index(item, start), end=' ')  # Вывод наибольших
      start = arr.index(
        item) + 1  # Метод index выводит первый подходящий по запросу, поэтому берется последний найденный элемент(его индекс) и делаеться исключение, по началу входа


# Список абонентов сети кабельного телевидения состоит из элементов следующей структуры:
# фамилия, район, адрес, телефон, номер договора, дата заключения договора, оплата установки,
# дата последнего платежа. Поиск и сортировка — по району, номеру договора, дате последнего платежа.

class Users:
  _users = []  # Список абонентов

  def adduser(self, lastname, district, address, phone, contract_number, date_of_the_agreement, price,
              data_last_payment):  # добавление элементов в список
    instance = {
      'фамилия': lastname,
      'район': district,
      'адрес': address,
      'телефон': phone,
      'номер договора': contract_number,
      'дата заключения договора': date_of_the_agreement,
      'оплата установки': price,
      'дата последнего платежа': data_last_payment
    }
    self._users.append(instance)

  def printer(self):  # Просто вывод
    for item in self._users:
      print(item)

  def sorting(self, oper):  # Сортировка по аргумену, где "oper" это аргумент по которорму идет сортеровка
    print(f'Сортировака по "{oper}"')
    check = True  # Ограничитель
    while check:  # Потребность в сортироваке
      check = False  # Чтобы не был безконечный цикл

      for item in range(len(self._users) - 1):  # Берется вся длина списка, по которой будет происходлить сортеровка
        if self._users[item][oper] > self._users[item + 1][oper]:  # Берутся 2 рядостоящих элемента
          self._users[item], self._users[item + 1] = self._users[item + 1], self._users[
            item]  # Если левый элемент больше чем правый, они меняються местами
          check = True  # Если не было входов в цикл, то он заканчиваеться

  def search(self, oper, arg):  # Поиск по аргументу
    checked = True  # переменная для проверки
    print(f'Поиск по "{oper}"')

    for item in self._users:  # проходимся по всему списку
      if item[oper] is arg:
        checked = False  # если был вход в условие данные найдены
        print(item)

    if checked:  # если не было входа в предидущее условие, то данных нет
      print('По запросу нет данных')


# 8. Сформировать стек из N чисел. Найти произведение второго и третьего чисел. Результат поместить в стек.

def creature_stek(num):  # num длина стека
  stek = [random.randint(-30, 30) for item in range(num)]  # аналогия стека, заполняется рандомно
  shadow_stek = []  # Стек для переноса (вспомогательный)
  value = len(stek) - 1  # Переменная длины стека
  counting = int()  # переменная для конечной суммы 2 и 3 элемента

  print(f"Исходный стек {list.copy(stek)}")  # Вывод данных

  for item in range(len(stek)):  # цикл по всей длине первого стека
    if value == 1 or value == 2:  # Поиск исключительно 2 и 3 числа из стека
      counting += stek.pop()  # Если найдено, то прибавляются друг к другу

    else:  # Если нет, то просто переносится вспомогательный стек
      shadow_stek.append(stek.pop())

    value -= 1

  print(f"Сумма 2 и 3 чисел {counting}")  # Вывод данных

  for item in range(len(shadow_stek)):  # Обратно заполнение исходного стека
    stek.append(shadow_stek.pop())
  stek.append(counting)
  print(f'Конечный выход {stek}')  # Вывод данных


if __name__ == '__main__':
  # №1
  print(positive_number_between_negative(10), '\n')

  # №2
  arr = ['Hello', 'Hello world', 'Hi', 'Hallo', 'Hello world']
  comparison_of_lengths(arr)

  # №3
  import names  # Рандомные имена
  import random_address  # Рандомные адреса
  import phone_gen  # Рандомные телефонные номера
  import datetime, random  # Рандомные даты

  user = Users()
  districtExample = ['Красногорский', 'Динарский', 'Пригородный']
  contract_numberExample = ['No-102030', 'No-202020', 'No-123030', 'No-111111']

  for i in range(10):
    user.adduser(
      f"{names.get_last_name()}",
      f"{districtExample[random.randint(0, 2)]}",
      f"{random_address.real_random_address_by_state('CA')['address1']}",
      f"{phone_gen.PhoneNumber('DE').get_national()}",
      f"{contract_numberExample[random.randint(0, 3)]}",
      f"{datetime.date(random.randint(2020, 2021), random.randint(1, 12), random.randint(1, 30))}",
      # ValueError: day is out of range for month
      f'{random.randrange(5000, 10000, 500)} Pуб.',
      f"{datetime.date(random.randint(2022, 2023), random.randint(1, 12), random.randint(1, 30))}"
      # ValueError: day is out of range for month
    )
  print('\n')
  user.printer()  # Изначальный список

  user.sorting('район')  # Сортировка по району
  user.printer()

  user.sorting('номер договора')  # Сортировка по номеру договора
  user.printer()

  user.sorting('дата последнего платежа')  # Сортировка по дате последнего платежа
  user.printer()

  user.search('район', 'Красногорский')  # Поиск по району
  user.search('номер договора', 'No-202020')  # Поиск по номеру договора
  user.search('дата последнего платежа', '2022-03-04')  # Поиск по дате платежа

  # №4
  print('\t')
  creature_stek(10)