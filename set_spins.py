from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox
from PyQt5.QtGui import QFont

from coordinates import x, y, y_margin, padding_spins


class SetSpins():

    def __init__(self):                         # Показываю какие методы используются в классе
        self.set_spin_boxes()   

    def set_spin_boxes(self):                   # Метод создания объектов полей ввода чисел

        self.spins = []
        ranges = [(100_000, 25_000_000), (0, 25_000_000), (1, 25), (0.1, 25)]

        for i in range(0, len(ranges)):

            if (i != 3):
                self.spins.append(QSpinBox(self))
            else:
                self.spins.append(QDoubleSpinBox(self))
                self.spins[i].setSingleStep(0.1)

            self.spins[i].setFont(QFont('Times', 18, 12, False))
            self.spins[i].resize(250, 25) 
            self.spins[i].move(x, y + padding_spins + y_margin * i)
            self.spins[i].setRange(ranges[i][0], ranges[i][1])

                                                    # Установка новых значений исходя из положения слайдеров
    def set_new_value1(self, value1):
        self.spins[0].setValue(value1)
    def set_new_value2(self, value2):
        self.spins[1].setValue(value2)
    def set_new_value3(self, value3):
        self.spins[2].setValue(value3)
    def set_new_value4(self, value4):
        self.spins[3].setValue(value4 / 10)
        

    def change_value_1_1(self):
        self.spins[1].setValue(self.spins[0].value() * 0)
    def change_value_1_2(self):
        self.spins[1].setValue(int(self.spins[0].value() * 0.1))
    def change_value_1_3(self):
        self.spins[1].setValue(int(self.spins[0].value() * 0.15))
    def change_value_1_4(self):
        self.spins[1].setValue(int(self.spins[0].value() * 0.2))
    def change_value_1_5(self):
        self.spins[1].setValue(int(self.spins[0].value() * 0.25))
    def change_value_1_6(self):
        self.spins[1].setValue(int(self.spins[0].value() * 0.30))

    def change_value_2_1(self):
        self.spins[2].setValue(5)
    def change_value_2_2(self):
        self.spins[2].setValue(10)
    def change_value_2_3(self):
        self.spins[2].setValue(15)
    def change_value_2_4(self):
        self.spins[2].setValue(20)
        
    def change_value_3_1(self):
        self.spins[3].setValue(0.1)
    def change_value_3_2(self):
        self.spins[3].setValue(4.5)
    def change_value_3_3(self):
        self.spins[3].setValue(6)
    def change_value_3_4(self):
        self.spins[3].setValue(7)
    def change_value_3_5(self):
        self.spins[3].setValue(7.3)
    def change_value_3_6(self):
        self.spins[3].setValue(7.5)
    def change_value_3_7(self):
        self.spins[3].setValue(9.1)
    def change_value_3_8(self):
        self.spins[3].setValue(10)