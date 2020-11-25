# класс - чертёж
class Auto:
    # метод
    def go_ahead(self):
        print(f'{self.color} автомобиль {self.model} едет вперёд на скорости {self.speed} км/ч')

    def set_new_auto(self, model, speed, color):
        self.model = model
        self.speed = speed
        self.color = color

class Bus(Auto):
    def set_bus(self, model, speed, color, seats):
        self.set_new_auto(model, speed, color)
        self.seats = seats
    
    def bus_info(self):
        self.go_ahead()
        print(f'Количество мест: {self.seats}')


    

my_car = Auto()
my_car.set_new_auto('volvo XC90', 200, 'черный')
my_car.go_ahead()

mother_car = Auto()
mother_car.set_new_auto('Lexus x200', 220, 'синий')
mother_car.go_ahead()

some_bus = Bus()
some_bus.set_bus('SCANIA', 180, 'белый', 60)
some_bus.bus_info()





    