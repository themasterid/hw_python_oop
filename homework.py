import datetime as dt


class Record:
    """Класс запись."""
    date_format = '%d.%m.%Y'
    now = dt.datetime.now()

    def __init__(self, amount: int, comment: str, date: str = str(now.date())):
        self.amount = amount
        self.comment = comment
        self.date = date
        self.records: list = list()

    def add_record(self) -> list:
        self.records.append([self.amount, self.comment, self.date])
        return self.records


class Calculator:
    """Базовый класс калькулятора колорий."""
    def __init__(self, limit):
        self.limit = limit

    def add_record(self):
        pass

    def get_today_stats(self):
        pass

    def get_today_cash_remained(self, currency: str) -> str:
        pass

    def get_week_stats(self):
        pass

    def show(self):
        print(f'Запись в Calculator - {self.limit}')


class CaloriesCalculator(Calculator):
    """Класс калькулятора колорий."""
    def __init__(self, limit):
        super().__init__(limit)
        #self.limit: int = limit

    def get_calories_remained(self):
        if self.limit < 1000:
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit} кКал')
        else:
            print('Хватит есть!')


class CashCalculator(Calculator):
    """Класс калькулятора денег."""
    def __init__(self, currency):
        super().__init__(currency)
        self.currency = currency


    def get_today_cash_remained(self):
        print(f'На сегодня осталось {self.currency} руб/USD/Euro')
        print('Денег нет, держись')
        print('Денег нет, держись: твой долг - N руб/USD/Euro')


r1 = Record(amount=145, comment='Безудержный шопинг')
r2 = Record(amount=1568,
            comment='Наполнение потребительской корзины',
            date='09.03.2019')
r3 = Record(amount=691, comment='Катание на такси', date='08.03.2019')
print(r1.add_record())
print(r2.add_record())
print(r3.add_record())
calc = Calculator(1000)
cash_calculator = CashCalculator(1000)
colories_calculator = CaloriesCalculator(10000)
calc.show()
cash_calculator.show()
colories_calculator.get_calories_remained()
cash_calculator.get_today_cash_remained(100)
'''
# для CashCalculator 
r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
r2 = Record(amount=1568,
            comment='Наполнение потребительской корзины',
            date='09.03.2019')
r3 = Record(amount=691, comment='Катание на такси', date='08.03.2019')

# для CaloriesCalculator
r4 = Record(amount=1186,
            comment='Кусок тортика. И ещё один.',
            date='24.02.2019')
r5 = Record(amount=84, comment='Йогурт.', date='23.02.2019')
r6 = Record(amount=1140, comment='Баночка чипсов.', date='24.02.2019') 
# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))
# должно напечататься
# На сегодня осталось 555 руб 


date_format = '%d.%m.%Y'
moment = dt.datetime.strptime('16.12.2019', date_format)
print(moment)
# напечатает что-то вроде 2019-12-16 00:00:00

day = moment.date()
print(day)
# напечатает дату: 2019-12-16

now = dt.datetime.now()
print(now)
# напечатает время на текущий момент в формате: 2019-01-31 13:33:27.506227

print(now.date()) 
# напечатает текущую дату: 2019-01-31 

'''