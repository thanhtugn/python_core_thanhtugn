class Vehicle:
    def __init__(self, Name_, max_speed_):
        self.__Name = Name_
        self.__max_speed = max_speed_

    def get_veh(self):
        print(f'Name: {self.__Name}')
        print(f'Max speed: {self.__max_speed}')


    def set_veh(self, Name_, max_speed_):
        self.__Name = Name_
        self.__max_speed = max_speed_

    def check_speed(self):
        if self.__max_speed > 70:
            print('Speed: Fast')
        elif self.__max_speed >= 30:
            print('Speed: Normal')
        else:
            print('Speed: Slow')
print('-------------------------------')
print('------------NEW----------------')
veh_1 = Vehicle('Ford',70)
veh_1.get_veh()
veh_1.check_speed()
print('------------NEW----------------')
veh_2 = Vehicle('BMW', 30)
veh_2.get_veh()
veh_2.check_speed()
print('-------------------------------')
print('------------UPDATE-------------')
veh_1.set_veh('Ford',100)
veh_1.get_veh()
veh_1.check_speed()
print('------------UPDATE-------------')
veh_2.set_veh('BMW', 50)
veh_2.get_veh()
veh_2.check_speed()
print('-------------------------------')



        
        



        