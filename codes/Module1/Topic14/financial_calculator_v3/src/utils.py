def format_money(money_symbol, decimal_places, amount):
    if amount >= 0:
        return f"{money_symbol}{amount:.{decimal_places}f}"
    else:
        return f"-{money_symbol}{abs(amount):.{decimal_places}f}"