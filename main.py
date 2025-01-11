import sys
from PyQt5.QtWidgets import QDialog, QApplication, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from set_sliders import SetSliders
from set_buttons import SetButtons


class DlgMain(QDialog, SetButtons, SetSliders):                                     # Наследование от главного класса библиотеки PyQt5 - QDIalog
                                                                               # и наследование методов создания объектов из импортируемых файлов 
    def __init__(self):
        super().__init__()
        self.set_window_title(img_pic="images/red_hearth.ico")                 # Настройка заголовка и иконки окна        
        self.set_backgrounf_image(img_jpg="images/backg.jpg")                  # Настройка заднего фона и подгонка окна по размерам изображения
        self.left_side_text()                                                  # Вызов функции создания текста с левой стороны из SetText
        self.right_side_text()
        self.set_spin_boxes()                                                  # Вызоф функции создания полей для чисел SetSpins
        self.left_side_sliders()
        self.set_left_buttons1()
        self.set_left_buttons2()
        self.set_left_buttons3()
        self.set_right_button()
        

    def set_window_title(self, img_pic):
        self.setWindowTitle("Финансовый калькулятор")                   # Название окна
        self.setWindowIcon(QIcon(img_pic))                              # Установить иконку для приложения


    def set_backgrounf_image(self, img_jpg):
        label = QLabel(self)                                            # Создание поверхности для обьектов
        pixmap = QPixmap(img_jpg)                                       # Создание Pixmap изображения
        label.setPixmap(pixmap)                                         # Установка изображения на поверхность
        self.setFixedSize(pixmap.width(), pixmap.height())              # Подгонка размеров окна под изображение с фиксированным значением



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())