class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def inf(self):
        print('Название автомобиля: {}; Скорость: {}; Пробег: {}'.format(self.name, self.max_speed, self.mileage))
#Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
#Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12
while True:
    n = input('Название автомобиля: ')
    max_s = (input('Максемальная скорость автомобиля: '))
    m = (input('Пробег: '))
    if (not n) or (not max_s) or (not m):
        break
    else:
        Autobus = Transport(n, max_s, m)
        Autobus.inf()
   


