import datetime as dt
from typing import Union


class Record:
    """Класс для хранения значений."""

    def __init__(
        self,
        amount: int,
        comment: str,
        date: Union[str, None] = None
    ) -> None:
        self.amount: int = amount
        self.comment: str = comment
        self.date: dt.date = dt.datetime.now().date()
        if date is not None:
            self.date = dt.datetime.strptime(str(date), '%d.%m.%Y').date()


class Calculator:
    """Базовый класс калькулятора калорий и денег."""

    def __init__(self, limit: Union[float, int]):
        self.limit: Union[float, int] = limit
        self.records: list = list()
        self.today_d = dt.date.today()

    def add_record(self, obj: object):
        return self.records.append(obj)

    def get_today_stats(self):
        return sum([
            day.amount for day in self.records
            if day.date == self.today_d])

    def get_week_stats(self):
        offset_week = self.today_d - dt.timedelta(days=7)
        return sum([
            day.amount for day in self.records
            if offset_week <= day.date <= self.today_d])


class CaloriesCalculator(Calculator):
    """Дочерний класс калькулятора калорий."""

    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self) -> str:
        calories_today: Union[float, int] = self.get_today_stats()
        msg_stop_eat: str = 'Хватит есть!'
        msg_go_eat: str = (
            f'Сегодня можно съесть что-нибудь ещё, '
            f'но с общей калорийностью не более'
            f' {self.limit - calories_today} кКал')
        return msg_go_eat if calories_today < self.limit else msg_stop_eat


class CashCalculator(Calculator):
    """Дочерний класс калькулятора денег."""

    USD_RATE = 60.0
    EURO_RATE = 70.0

    def __init__(self, limit: Union[float, int]):
        super().__init__(limit)

    def get_today_cash_remained(self, currency: str) -> str:
        limittoday: Union[float, int] = self.limit - self.get_today_stats()
        self.currency: str = currency
        msg_no_money: str = 'Денег нет, держись'

        money: dict = {
            'rub': 'руб',
            'usd': 'USD',
            'eur': 'Euro'
        }

        try:
            money[self.currency]
        except KeyError:
            return '<выбрана неверная валюта>'

        if money[self.currency] == 'руб':
            cash_tday = limittoday
        elif money[self.currency] == 'USD':
            cash_tday = limittoday / self.USD_RATE
        else:
            cash_tday = limittoday / self.EURO_RATE

        if limittoday > 0:
            return (f'На сегодня осталось '
                    f'{round(cash_tday, 2)} {money[self.currency]}')
        elif limittoday < 0:
            return (f'{msg_no_money}: твой долг - '
                    f'{abs(round(cash_tday, 2))} {money[self.currency]}')
        else:
            return msg_no_money
