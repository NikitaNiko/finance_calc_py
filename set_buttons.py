from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from set_text import  SetText
from create_schedule import creating
from coordinates import x, y, y_margin, btn_weight, btn_height, x_r

class SetButtons(SetText):
    
    def __init__(self):
        self.set_left_buttons1()
        self.set_left_buttons2()
        self.set_left_buttons3()

    def set_left_buttons1(self):                            #Создание кнопок 1

        btns = []
        actions = [self.change_value_1_1, self.change_value_1_2, self.change_value_1_3, self.change_value_1_4, self.change_value_1_5, self.change_value_1_6]
        texts = ["0%", "10%", "15%", "20%", "25%", "30%"]
        for i in range(0, len(texts)):
            btns.append(QPushButton(texts[i], self))
            btns[i].resize(btn_weight + 10, btn_height)
            btns[i].move(x + btn_weight * i, y + y_margin + 85)
            btns[i].setFont(QFont('Sitka Small', 10, 12, False))
            btns[i].clicked.connect(actions[i])
        

    def set_left_buttons2(self):
            
        btns = []
        actions = [self.change_value_2_1, self.change_value_2_2, self.change_value_2_3, self.change_value_2_4]
        texts = ["5 лет", "10 лет", "15 лет", "20 лет"]
        for i in range(0, len(texts)):
            btns.append(QPushButton(texts[i], self))
            btns[i].resize(btn_weight + 15, btn_height)
            btns[i].move(x + (btn_weight + 10) * i, y + y_margin * 2 + 85)
            btns[i].setFont(QFont('Sitka Small', 10, 12, False))
            btns[i].clicked.connect(actions[i])

    
    def set_left_buttons3(self):

        btns = []
        actions = [self.change_value_3_1, self.change_value_3_2, self.change_value_3_3, self.change_value_3_4, self.change_value_3_5, self.change_value_3_6, self.change_value_3_7, self.change_value_3_8]
        texts = ["0,1%", "4,5%", "6%", "7%", "7,3%", "7,5%", "9,1%", "10%"]
        for i in range(0, len(texts)):
            btns.append(QPushButton(texts[i], self))
            btns[i].resize(btn_weight + 10, btn_height)
            btns[i].move(x + btn_weight * i, y + y_margin * 3 + 85)
            btns[i].setFont(QFont('Sitka Small', 10, 12, False))
            btns[i].clicked.connect(actions[i])


    
    def set_right_button(self):

        self.big_btn = QPushButton("Вывести график платежей", self)
        self.big_btn.move(x_r, 420)
        self.big_btn.resize(475, 50)
        self.big_btn.setFont(QFont('Sitka Small', 18, 16, False))
        self.big_btn.setStyleSheet("background-color: #2b2727; border-radius: 5px; border: 2px solid #02cbe6; color: #02cbe6;")
        self.big_btn.clicked.connect(self.calculate)                                  

        self.big_btn2 = QPushButton("Создать файл графика платежей", self)
        self.big_btn2.move(x_r, 495)
        self.big_btn2.resize(475, 50)
        self.big_btn2.setFont(QFont('Sitka Small', 18, 16, False))
        self.big_btn2.setStyleSheet("background-color: #2b2727; border-radius: 5px; border: 2px solid #02cbe6; color: #02cbe6;")
        self.big_btn2.clicked.connect(self.schedule)                                  # Вызов функции, которая находится в set_text
        self.big_btn2.hide()
        

    def calculate(self):

        self.kredit = self.spins[0].value() - self.spins[1].value()                                                             # Это займ
        self.n = self.spins[2].value() * 12                                                                                     # Это количество месяцев, за которые будут произврдится выплаты
        self.r = self.spins[3].value() / 100 / 12                                                                               # Это месячная процентная ставка
        self.monthly_pay = round(self.kredit * (self.r * (1 + self.r)**self.n) / (((1 + self.r)**self.n) - 1), 2)               # Ежемесячный платеж
        self.percents = round(self.monthly_pay * self.n - self.kredit, 2)                                                       # Сколько придется переплатить
        self.percents_and_kredit = round(self.monthly_pay * self.n, 2)                                                          # Общая сумма долга банку

        if (self.kredit < 0):
            QMessageBox.critical(self, "Ошибка", "Кредит не может быть отрицательным!")
            return

        self.items[0].setText(f"{self.texts[0]}{self.monthly_pay} P")
        self.items[1].setText(f"{self.texts[1]}{self.kredit} P")
        self.items[2].setText(f"{self.texts[2]}{self.percents} P")
        self.items[3].setText(f"{self.texts[3]}{self.percents_and_kredit} P")
        self.items[4].setText(f"{self.texts[4]}{self.monthly_pay * 2} P")

        self.big_btn2.show()

    def schedule(self):
        self.directory = QFileDialog.getSaveFileName(self, "Save to", "schedule", "Excel files (*.xlsx)")[0]
        if (self.directory):
            creating(self.n, self.percents_and_kredit, self.r, self.monthly_pay, self.directory)
        

