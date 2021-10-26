# Task 4.7
# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions
# (comparison, division, multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores information
# about exchange rates to your default currency:

# exchange_rate = {
#    "EUR": 0.93,
#    "BYN": 2.1,
#    ...
# }

# Example:
# x = Money(10, "BYN")
# y = Money(11) # define your own default value, e.g. “USD”
# z = Money(12.34, "EUR")
# print(z + 3.11 * x + y * 0.8) # result in “EUR”
# >>543.21 EUR

# lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
# s = sum(lst)
# print(s) #result in “BYN”
# >>123.45 BYN


import requests


# rates = {'BYN': 1, 'AUD': 1.8195, 'AMD': 5.1269, 'BGN': 1.4888, 'UAH': 9.4427, 'DKK': 3.9156, 'USD': 2.515, 'EUR': 2.9142, 'PLN': 6.3495, 'JPY': 2.263, 'IRR': 5.9881, 'ISK': 1.9427, 'CAD': 1.9802, 'CNY': 3.9013, 'KWD': 8.3397, 'MDL': 1.4318, 'NZD': 1.7367, 'NOK': 2.888, 'RUB': 3.4532, 'XDR': 3.5433, 'SGD': 1.8518, 'KGS': 2.9649, 'KZT': 5.8961, 'TRY': 2.8378, 'GBP': 3.3947, 'CZK': 11.5129, 'SEK': 2.8656, 'CHF': 2.6958}


def exchange_rate():
    response = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0').json()
    rates = {'BYN': 1}
    default_currency = 'BYN'

    for item in response:
        rates.update({item["Cur_Abbreviation"]: item["Cur_OfficialRate"]})

    return rates


class Money():

    def __init__(self, amount, currency='BYN'):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return f'{self.amount} {self.currency}'

    def convertion(self, to_currency):
        result = Money(0, self.currency)
        result.amount = self.amount * rates[self.currency] / rates[to_currency]
        result.currency = to_currency
        # return f'{self.amount} {from_currency} is {self.result} {to_currency}'
        return result

    def __add__(self, value):
        result = Money(0, self.currency)
        result.amount = self.amount + value.convertion(self.currency).amount
        result.currency = self.currency
        return result

    def __sub__(self, value):
        result = Money(0, self.currency)
        result.amount = self.amount - value.convertion(self.currency).amount
        result.currency = self.currency
        return result

    def __mul__(self, multiplier):
        result = Money(0, self.currency)
        result.amount = multiplier * self.amount
        result.currency = self.currency
        return result

    def __rmul__(self, multiplier):
        result = Money(0, self.currency)
        result.amount = multiplier * self.amount
        result.currency = self.currency
        return result

    def __le__(self, value):
        return self.amount <= value.convertion(self.currency).amount

    def __lt__(self, value):
        return self.amount < value.convertion(self.currency).amount

    def __eq__(self, value):
        return self.amount == value.convertion(self.currency).amount

    def __div__(self, divisor):
        result = Money(0, self.currency)
        result.amount = self.amount / divisor
        result.currency = self.currency
        return result

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)


rates = exchange_rate()
eur = Money(100, 'EUR')
byn = Money(50)
usd = Money(10, 'USD')
print(byn + usd, '+')
print(usd.convertion('BYN'))
print(byn + eur)
print(byn >= eur)
print(usd*20)
print(byn == usd)
print('sum=',sum([usd, byn, eur]))
x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”