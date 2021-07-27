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
    def __init__(self, limit: int, records: list = []):
        self.limit = limit
        self.records = records


class CaloriesCalculator(Calculator):
    """Класс калькулятора колорий."""
    def __init__(self, limit):
        super().__init__(limit)

    def add_record(self):
        pass

    def get_today_stats(self):
        pass

    def get_calories_remained(self):
        if self.limit < 1000:
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit} кКал')
        else:
            print('Хватит есть!')

    def get_week_stats(self):
        pass


class CashCalculator(Calculator):
    """Класс калькулятора денег."""
    def __init__(self, limit):
        super().__init__(limit)


    def add_record(self):
        pass

    def get_today_stats(self):
        pass

    def get_today_cash_remained(currency):
        print('На сегодня осталось 1 руб/USD/Euro')
        print('Денег нет, держись')
        print('Денег нет, держись: твой долг - N руб/USD/Euro')

    def get_week_stats(self):
        pass


cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment='кофе'))