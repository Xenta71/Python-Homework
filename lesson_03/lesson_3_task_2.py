from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Redmi 8", "+79101234567"),
    Smartphone("Iphone", "14 pro", "+79153214567"),
    Smartphone("Iphone", "15 max", "+79209058888"),
    Smartphone("Realme", "12", "+793091218793"),
    Smartphone("Honor", "10i", "+79053006766")
]

for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model}. {Smartphone.sub_number}")