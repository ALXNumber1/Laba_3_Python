with open('Вокзал.txt', 'r', encoding='utf-8') as file:
    trains = file.readlines()

def trains_by_day(day):
    print(f'Поезда, отправляющиеся в {day}:')
    for train in trains:
        train_info = train.split()
        if train_info[2] == day:
            print(train)

def max_ticket_price_train():
    max_price = 0
    max_price_train = None
    for train in trains:
        train_info = train.split()
        price = int(train_info[-1])
        if price > max_price:
            max_price = price
            max_price_train = train
    print(f"Поезд с максимальной стоимостью билета: {max_price_train}")

trains_by_day('понедельник')
max_ticket_price_train()