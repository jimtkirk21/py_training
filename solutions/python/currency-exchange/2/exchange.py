"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget: float, exchange_rate: float) -> float:
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    if not isinstance(budget, (int, float)):
        raise TypeError(f"budget must be a number, got {type(budget).__name__}")
    if not isinstance(exchange_rate, (int, float)):
        raise TypeError(f"exchange_rate must be a number, got {type(exchange_rate).__name__}")
    changed_money = budget / exchange_rate
    return changed_money


def get_change(budget: float, exchanging_value: float) -> float:
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    if not isinstance(budget, (int, float)):
        raise TypeError(f"budget must be a number, got {type(budget).__name__}")
    if not isinstance(exchanging_value, (int, float)):
        raise TypeError(f"exchange_rate must be a number, got {type(exchanging_value).__name__}")
    return budget-exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return int(denomination * number_of_bills)


def get_number_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return float(amount % denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    effective_rate = exchange_rate * (1 + spread / 100)
    total_target = budget / effective_rate
    count = int(total_target // denomination)
    return int(count * denomination)
#int((budget/((spread*exchange_rate)+exchange_rate))//denomination)*denomination
