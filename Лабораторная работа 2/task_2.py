salary = 5000
spend = 6000
months = 10
increase = 0.03

money_capital = 0
current_spend = spend

for month in range(months):
    needed_money = current_spend - salary
    if needed_money > 0:
        money_capital += needed_money
    current_spend += current_spend * increase

money_capital = round(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
