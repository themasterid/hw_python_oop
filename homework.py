import datetime as dt


class Record:
    """Класс запись занчений."""
    def __init__(self, amount: int, comment: str, date: str = dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        self.date = date
        self.records: list = list()

    def add_record(self, obj):
        self.obj = obj
        self.records.append(self.obj)


class Calculator:
    """Базовый класс калькулятора колорий."""
    def __init__(self, limit):
        self.limit = limit
        self.records: list = list()

    def add_record(self, obj):
        self.obj = obj
        self.records.append(self.obj)

    def get_today_stats(self):
        count_today = 0
        for i in self.records:
            if i.date == dt.datetime.now().date():
                count_today += i.amount
        return count_today

    def get_week_stats(self):
        pass


class CaloriesCalculator(Calculator):
    """Класс калькулятора колорий."""
    def __init__(self, limit):
        self.limit = limit
        self.records: list = list()

    def get_calories_remained(self):
        count_today = 0
        for i in self.records:
            if i.date == dt.datetime.now().date():
                count_today += i.amount
        return count_today

        #if self.limit < 1000:
        #    return ('''Сегодня можно съесть что-нибудь ещё, но с общей
        #    калорийностью не более {0} кКал'''.format(self.limit))
        #else:
        #    return 'Хватит есть!'


class CashCalculator(Calculator):
    """Класс калькулятора денег. 'rub', 'usd' или 'eur'"""
    USD_RATE = 424.60
    EURO_RATE = 500.90

    def __init__(self, limit):
        self.limit = limit
        self.records: list = list()

    def get_today_cash_remained(self, currency: str):
        self.limittoday = self.limit
        self.currency = currency

        for i in self.records:
            if i.date == dt.datetime.now().date():
                self.limittoday -= i.amount

        if self.limittoday > 0:
            return f'На сегодня осталось {self.limittoday} {self.currency}'
        elif self.limittoday == 0:
            return 'Денег нет, держись'
        else:
            return 'Денег нет, держись: твой долг - {0} {1}'.format(
                abs(self.limittoday), currency)


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CaloriesCalculator(2500)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=1000, comment='Тестовый коммент', date='01.09.2019'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

print(cash_calculator.get_calories_remained())
# должно напечататься
# На сегодня осталось 555 руб 