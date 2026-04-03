from address import Address
from mailing import Mailing

to_adress = Address(354340, "Sochi", "Lenina", 1, 15)
from_address = Address(427430, "Votkinsk", "Lenina", 1, 8)
cost = 587
track = "0123456"

mailing = Mailing(to_adress, from_address, cost, track)

print(mailing)
