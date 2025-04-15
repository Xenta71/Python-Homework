from address import Address
from mailing import Mailing

to_address = Address("606130", "Павлово", "Фаворского", "62", "42")
from_address = Address("603000", "Нижний Новгород", "Ленина", "19", "23")

mailing = Mailing(to_address, from_address, 500, "8001267090")

print(f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. Стоимость {mailing.cost} рублей.")