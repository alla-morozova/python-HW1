from address import Address
from mailing import Mailing

to_address = Address("12122", "Москва", "Михалковская", "44", "36")
from_address = Address("34355", "Луганск", "Кирова", "2", "11")
cost = 1111
track = "112121A"

mailing = Mailing(to_address, from_address, cost, track)
print(f"Отправление {track} из {from_address} в {to_address}. Стоимость {cost} рублей.")
