salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен #В условии сказано, что increase 5%

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

new_spend = spend
all_salary = salary * months
for _ in range(months - 1):
    spend += spend * increase
    new_spend += spend
money_capital = round(new_spend - all_salary)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

