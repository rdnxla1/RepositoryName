money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
remain = salary - spend
inflation = 1.05

while money_capital + remain >= spend:
    money_capital += remain
    spend *= inflation

    month +=1

# TODO Оформить решение

print(month)
