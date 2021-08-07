import datetime as dt
import sys
from typing import Optional, Union

from PyQt5 import QtWidgets

from mainwindows import Ui_CalcWin

DATE_FMT: str = '%d.%m.%Y'
MONEY: dict = {'rub': 'руб', 'usd': 'USD', 'eur': 'Euro'}
USD_RATE: float = 72.0
EURO_RATE: float = 86.0
RUB_RATE: float = 1.0


class Record:
    """Класс для хранения значений."""

    def __init__(
        self,
        amount: int,
        comment: str,
        date: Optional[str] = None
    ) -> None:
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, DATE_FMT).date()
        else:
            self.date = dt.datetime.now().date()


class Calculator(QtWidgets.QMainWindow):
    """"Базовый класс калькулятора калорий и денег."""

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_CalcWin()
        self.ui.setupUi(self)
        self.limit = int(self.ui.limit_e.text())
        self.records: list = []

        self.ui.add_rec_b.clicked.connect(self.add_record)

        self.ui.week_r_b.clicked.connect(self.get_week_stats)
        self.ui.day_r_b.clicked.connect(self.get_today_stats)

        self.ui.ostatok_mon_b.clicked.connect(
            lambda: CashCalculator.get_today_cash_remained(self))

        self.ui.ostatok_cal_b.clicked.connect(
            lambda: CaloriesCalculator.get_calories_remained(self))

    def add_record(self) -> None:
        amount = int(self.ui.rashod_e.text())
        comment = self.ui.comm_e.text()
        date = self.ui.date_e.text()
        self.records.append(
            Record(amount, comment, date)
        )
        self.statusBar().showMessage(
            f'Добавлено записей - {str(len(self.records))}')

    def get_today_stats(self) -> Union[int, float]:
        curency = self.ui.curency_e.text()
        today = dt.date.today()
        out = sum(
            day.amount for day in self.records
            if day.date == today)
        self.ui.resoult_txt.setText(
            f'Расход в день - {out} {MONEY[curency]}/кКал')
        return out

    def get_week_stats(self) -> Union[int, float]:
        today = dt.date.today()
        offset_week = today - dt.timedelta(days=7)
        curency = self.ui.curency_e.text()
        out = sum(
            day.amount for day in self.records
            if offset_week <= day.date <= today)
        self.ui.resoult_txt.setText(
            f'Расход в неделю - {out} {MONEY[curency]}/кКал')
        return out

    def get_limit_today(self) -> Union[int, float]:
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    """Дочерний класс калькулятора калорий."""

    def get_calories_remained(self):
        limit_today = self.get_limit_today()
        if limit_today > 0:
            return self.ui.resoult_txt.setText(
                'Сегодня можно съесть что-нибудь ещё, но с общей '
                f'калорийностью не более {limit_today} кКал')
        return self.ui.resoult_txt.setText('Хватит есть!')


class CashCalculator(Calculator):
    """Дочерний класс калькулятора денег."""

    def get_today_cash_remained(self):
        money: dict = {
            'rub': (RUB_RATE, 'руб'),
            'usd': (USD_RATE, 'USD'),
            'eur': (EURO_RATE, 'Euro')
        }
        currency = self.ui.curency_e.text()
        if currency not in money:
            return self.ui.resoult_txt.setText('<выбрана неверная валюта>')

        limit_today = self.get_limit_today()

        if limit_today == 0:
            return self.ui.resoult_txt.setText('Денег нет, держись')

        rate_m, name_money = money[currency]

        cash_today = round(abs(limit_today) / rate_m, 2)

        if limit_today > 0:
            return self.ui.resoult_txt.setText(
                f'На сегодня осталось {cash_today} {name_money}')
        return self.ui.resoult_txt.setText(
            f'Денег нет, держись: твой долг - {cash_today} {name_money}')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Calculator()
    application.show()
    sys.exit(app.exec())
