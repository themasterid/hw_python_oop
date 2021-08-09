import datetime as dt
import json
import sys
from typing import Optional, Union

import requests
from bs4 import BeautifulSoup

from PyQt5.QtWidgets import QTableWidgetItem

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from mainwindows import Ui_CalcWin

DATE_FMT: str = '%d.%m.%Y'
TODAY = dt.date.today().strftime(DATE_FMT)
MONEY: dict = {
    'RUR': 'руб/кКал',
    'USD': 'USD/кКал',
    'EUR': 'Euro/кКал',
    'KZT': 'тенге/кКал'}
MONEY1: dict = {'RUR': 'руб', 'USD': 'USD', 'EUR': 'Euro', 'KZT': 'тенге'}


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
        self.date = (
            dt.datetime.strptime(date, DATE_FMT).date()
            if date
            else dt.datetime.now().date())


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

        self.ui.resoult_t.setColumnCount(3)
        self.ui.resoult_t.setRowCount(len(self.records))
        self.ui.resoult_t.setSortingEnabled(True)

        rows_list = []
        for _ in range(len(self.records)):
            rows_list.append(str(_ + 1))
        self.ui.resoult_t.setVerticalHeaderLabels(rows_list)

        row = 0
        for tup in self.records:
            col = 0
            for item in [
                str(tup.amount),
                tup.comment,
                tup.date.strftime(DATE_FMT)
            ]:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.resoult_t.setItem(row, col, cellinfo)
                col += 1
            row += 1

        self.ui.resoult_t.setGridStyle(1)
        # self.ui.resoult_t.resizeColumnsToContents()

    def get_today_stats(self) -> Union[int, float]:
        curency = self.ui.curency_e.currentText()
        today = dt.date.today()
        out = sum(
            day.amount for day in self.records
            if day.date == today)
        self.ui.resoult_txt.setText(
            f'Расход в день - {out} {MONEY[curency]}')
        return out

    def get_week_stats(self) -> Union[int, float]:
        curency = self.ui.curency_e.currentText()
        today = dt.date.today()
        offset_week = today - dt.timedelta(days=7)
        out = sum(
            day.amount for day in self.records
            if offset_week <= day.date <= today)
        self.ui.resoult_txt.setText(
            f'Расход в неделю - {out} {MONEY[curency]}')
        return out

    def get_limit_today(self) -> Union[int, float]:
        return self.limit - self.get_today_stats()

    def get_rates(self, cur_from, dates, requests):
        fname = f'currency_{TODAY}.json'
        if cur_from == 'RUR':
            return {'RUR': 1.0}

        if self.open_file(fname):
            return self.open_file(fname)

        result = requests.get(
            "https://www.cbr.ru/scripts/XML_daily.asp",
            {"date_req": dates})
        soup = BeautifulSoup(result.content, 'xml')
        rates = {i.CharCode.string: (
            float(i.Value.string.replace(',', '.'))
        ) for i in soup('Valute')
        }
        self.write_file(rates, fname)
        return self.open_file(fname)

    def write_file(self, r, fname):
        with open(fname, 'w', encoding='utf-8') as f:
            return json.dump(r, f, ensure_ascii=False, indent=4)

    def open_file(self, fname):
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return False


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
        limit_today = self.get_limit_today()

        if limit_today == 0:
            return self.ui.resoult_txt.setText('Денег нет, держись')

        today = dt.date.today().strftime("%d.%m.%Y")
        curency = self.ui.curency_e.currentText()
        rate_m = self.get_rates(curency, today, requests)
        cash_today = round(abs(limit_today) / rate_m[curency], 2)

        if limit_today > 0:
            return self.ui.resoult_txt.setText(
                f'На сегодня осталось {cash_today} {MONEY1[curency]}')
        return self.ui.resoult_txt.setText(
            f'Денег нет, держись: твой долг - {cash_today} {MONEY1[curency]}')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Calculator()
    application.show()
    sys.exit(app.exec())
