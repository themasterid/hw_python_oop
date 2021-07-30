import datetime as dt
from typing import Optional, Union


class Record:
    """Класс для хранения значений."""

    DATE_FMT: str = '%d.%m.%Y'

    def __init__(
        self,
        amount: int,
        comment: str,
        date: Optional[str] = None
    ) -> None:
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, self.DATE_FMT).date()
        else:
            self.date = dt.datetime.now().date()


class Calculator:
    """Базовый класс калькулятора калорий и денег."""

    def __init__(self, limit: Union[float, int]):
        self.limit = limit
        self.records: list = []

    def add_record(self, obj: Record) -> list:
        return self.records.append(obj)

    def get_today_stats(self) -> Union[int, float]:
        return sum(
            day.amount for day in self.records
            if day.date == dt.date.today())

    def get_week_stats(self) -> Union[int, float]:
        offset_week: dt.date = dt.date.today() - dt.timedelta(days=7)
        return sum(
            day.amount for day in self.records
            if offset_week <= day.date <= dt.date.today())

    def limit_today(self) -> Union[int, float]:
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    """Дочерний класс калькулятора калорий."""

    def get_calories_remained(self) -> str:
        if self.get_today_stats() < self.limit:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    'но с общей калорийностью не более'
                    f' {self.limit_today()} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    """Дочерний класс калькулятора денег."""

    USD_RATE: float = 60.0
    EURO_RATE: float = 70.0

    def get_today_cash_remained(self, currency: str) -> str:
        money: dict = {'rub': 'руб', 'usd': 'USD', 'eur': 'Euro'}

        if currency not in money:
            return '<выбрана неверная валюта>'

        if self.limit_today() == 0:
            return 'Денег нет, держись'
        else:
            if money[currency] == 'руб':
                cash_tday = abs(round(self.limit_today(), 2))
            elif money[currency] == 'USD':
                cash_tday = abs(round(self.limit_today() / self.USD_RATE, 2))
            else:
                cash_tday = abs(round(self.limit_today() / self.EURO_RATE, 2))

            if self.limit_today() > 0:
                return ('На сегодня осталось '
                        f'{cash_tday} {money[currency]}')
            else:
                return ('Денег нет, держись: твой долг - '
                        f'{cash_tday} {money[currency]}')
