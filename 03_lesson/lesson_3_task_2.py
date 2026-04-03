from smartphone import Smartphone

catalog = [
    Smartphone("1", "Apple", "+79011234567"),
    Smartphone("2", "Apple", "+79021234567"),
    Smartphone("3", "Apple", "+79031234567"),
    Smartphone("4", "Apple", "+79041234567"),
    Smartphone("5", "Apple", "+79051234567"),
]
for phone in catalog:
    print(f"{phone.mark} - {phone.model}. {phone.number}")
