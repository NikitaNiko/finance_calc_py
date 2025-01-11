from PyQt5.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui

from set_spins import SetSpins
from coordinates import x, y, y_margin, x_r, y_r, y_margin_r

class SetText(SetSpins):

    def __init__(self):                                     # Показываю какие методы используются в классе
        
        self.left_side_text()
        

    def left_side_text(self):                               # Создание и оформление текста                   
        texts = ["Стоимость недвижимости", "Первоначальный взнос", "Срок кредита", "Процентная ставка"]
        self.items = []

        for i in range(0, len(texts)):
            self.items.append(QLabel(self))
            self.items[i].setStyleSheet("color: #0cdb04; ")                       # Объявляю настройку цвета для текст
            self.items[i].setFont(QFont('Sitka Small', 22, 12, False))           # Объявляю фон
            self.items[i].move(x, y + y_margin * i)                              # По формуле каждый объект будет отдаляться друг от друга по заданным координатам и отступу!
            self.items[i].setText(texts[i])
            self.items[i].setGraphicsEffect(QGraphicsDropShadowEffect(self, blurRadius = 30, color = QtGui.QColor("#d2d9d2"), offset = QtCore.QPointF(0.0, 0.0)))


    def right_side_text(self):
        self.texts = ["Ваш ежемесячный платеж: ", "Кредит: ", "Проценты: ", "Проценты + кредит: ", "Необходимый доход: "]
        self.items = []

        for i in range(0, len(self.texts)):
            self.items.append(QLabel(self))
            self.items[i].setStyleSheet("color: #e85e02;")                      
            self.items[i].setFont(QFont('Sitka Small', 18, 12, False))
            self.items[i].move(x_r, y_r + y_margin_r * i)                              # По формуле каждый объект будет отдаляться друг от друга по заданным координатам и отступу!
            self.items[i].setText(self.texts[i])
            self.items[i].resize(550, 30)
            self.items[i].setGraphicsEffect(QGraphicsDropShadowEffect(self, blurRadius = 30, color = QtGui.QColor("#0cdb04"), offset = QtCore.QPointF(0.0, 0.0)))


    
        
