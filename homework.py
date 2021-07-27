import datetime as dt


class Record:
    """Класс запись занчений."""
    now = dt.datetime.now()

    def __init__(self, amount: int, comment: str, date: str = str(now.date())):
        self.amount = amount
        self.comment = comment
        self.date = date


class Calculator:
    """Базовый класс калькулятора колорий."""
    def __init__(self, limit):
        self.limit = limit
        self.records: list = list()


class CaloriesCalculator(Calculator):
    """Класс калькулятора колорий."""
    def __init__(self, limit):
        self.limit = limit

    def add_record(self, obj):
        return Record.add_record(obj)

    def get_today_stats(self):
        pass

    def get_calories_remained(self):
        if self.limit < 1000:
            return ('''Сегодня можно съесть что-нибудь ещё, но с общей
            калорийностью не более {0} кКал'''.format(self.limit))
        else:
            return 'Хватит есть!'

    def get_week_stats(self):
        pass


class CashCalculator(Calculator):
    """Класс калькулятора денег. 'rub', 'usd' или 'eur'"""
    USD_RATE = 424.60
    EURO_RATE = 500.90

    def __init__(self, limit):
        self.limit = limit
        self.records: list = list()
        self.now = dt.datetime.now()

    def add_record(self, obj):
        return self.records.append(obj)

    def get_today_stats(self):
        count_today = 0
        for i in self.records:
            if i.date == str(self.now.date()):
                count_today += i.amount
        return count_today

    def get_today_cash_remained(self, currency: str):
        self.limittoday = self.limit
        self.currency = currency

        for i in self.records:
            if i.date == str(self.now.date()):
                self.limittoday -= i.amount

        if self.limittoday > 0:
            return f'На сегодня осталось {self.limittoday} {self.currency}'
        elif self.limittoday == 0:
            return 'Денег нет, держись'
        else:
            return 'Денег нет, держись: твой долг - {0} {1}'.format(
                abs(self.limittoday), currency)

    def get_week_stats(self):
        pass
