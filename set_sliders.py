from PyQt5.QtWidgets import QSlider, QMessageBox
from PyQt5.QtCore import Qt
from set_spins import SetSpins

from coordinates import x, y, y_margin, padding_sliders

class SetSliders(SetSpins):

    def __init__(self):
        self.left_side_sliders()
        
                                                                # Создание ползунков для изменения значений поля ввода данных
    def left_side_sliders(self):
        

        bars = []
        ranges = [(100_000, 25_000_000), (0, 25_000_000), (0, 25), (0, 250)]
        defs = [self.set_new_value1, self.set_new_value2, self.set_new_value3, self.set_new_value4]         # Группа методов, вызывающих методы наследуемого класса SetSpins для изменения значений данных

        for i in range(0, len(ranges)):
            bars.append(QSlider(Qt.Orientation.Horizontal, self))
            bars[i].resize(250, 12)
            bars[i].setStyleSheet("QSlider::handle:horizontal {background-color: cyan; border: 1px solid black; border-radius: 4px; width: 4px;}")
            bars[i].move(x, y + padding_sliders + y_margin * i)
            bars[i].setRange(ranges[i][0], ranges[i][1])
            bars[i].setValue(250)
            bars[i].valueChanged.connect(defs[i])

                                                                        
   
        

          
