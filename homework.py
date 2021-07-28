import datetime as dt
from typing import Union


class Record:
    """Класс запись занчений."""

    def __init__(self, amt: int, comment: str, date: Union[str, None] = None):
        self.amount = amt
        self.comment = comment
        if date is None:
            date = dt.datetime.now().date()
        else:
            date = dt.datetime.strptime(str(date), '%d.%m.%Y').date()
        self.date = date

    def add_record(self, obj):
        self.obj = obj
        return self.records.append(self.obj)


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
            if i.date == dt.date.today():
                count_today += i.amount
        return count_today

    def get_week_stats(self):
        count_today = 0
        for i in self.records:
            if i.date == dt.date.today():
                count_today += i.amount
        return count_today


class CaloriesCalculator(Calculator):
    """Класс калькулятора колорий."""
    def __init__(self, limit):
        super().__init__(limit)
        self.limit = limit

    def get_calories_remained(self):
        count_today = 0
        for i in self.records:
            if i.date == dt.date.today():
                count_today += i.amount
        msg_go_eat: str = (
            f'Сегодня можно съесть что-нибудь ещё, '
            f'но с общей калорийностью не более'
            f' {self.limit - count_today} кКал')
        msg_stop_eat: str = 'Хватит есть!'
        return msg_go_eat if count_today < self.limit else msg_stop_eat


class CashCalculator(Calculator):
    """Класс калькулятора денег."""
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def __init__(self, limit):
        super().__init__(limit)
        self.limit = limit

    def get_today_cash_remained(self, currency: str):
        limittoday = self.limit
        self.currency = currency
        msg_no = 'Денег нет, держись'

        for i in self.records:
            if i.date == dt.date.today():
                limittoday -= i.amount

        if self.currency == 'rub':
            cash_s = 'руб'
            cash_tt = limittoday
        elif self.currency == 'usd':
            cash_s = 'USD'
            cash_tt = limittoday / self.USD_RATE
        elif self.currency == 'eur':
            cash_s = 'Euro'
            cash_tt = limittoday / self.EURO_RATE

        if limittoday > 0:
            return f'На сегодня осталось {round(cash_tt, 2)} {cash_s}'
        elif limittoday == 0:
            return msg_no
        else:
            return f'{msg_no}: твой долг - {abs(round(cash_tt, 2))} {cash_s}'


'''
#calc = Calculator(1000)
cal_calculator = CaloriesCalculator(1000)
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=999, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=2, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=1000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

cal_calculator.add_record(Record(
    amount=500,
    comment='бар в Танин др'))

cal_calculator.add_record(Record(
    amount=200,
    comment='бар в Танин др'))

cal_calculator.add_record(Record(
    amount=210,
    comment='бар в Танин др'))

print(cash_calculator.get_today_cash_remained('rub'))
print(cash_calculator.get_today_cash_remained('usd'))
print(cash_calculator.get_today_cash_remained('eur'))
print(cash_calculator.get_week_stats())
print(cal_calculator.get_week_stats())
'''
