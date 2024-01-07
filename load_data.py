from .models import EnergyConsumption

list1 = [
    EnergyConsumption(activity="Alvás",energyConsumption=0.93,note="-"),
    EnergyConsumption(activity="Fekvés",energyConsumption=1.10,note= "-"),
    EnergyConsumption(activity="Állás",energyConsumption=1.58,note= "-"),
    EnergyConsumption(activity="Gépkocsivezetés",energyConsumption=1.60,note= "-"),
    EnergyConsumption(activity="Séta",energyConsumption=2.75,note= "3 km/h sebességnél"),
    EnergyConsumption(activity="Gyaloglás",energyConsumption=3.70,note= "6 km/h sebességnél"),
    EnergyConsumption(activity="Háztartási munka",energyConsumption=3.43,note= "-"),
    EnergyConsumption(activity="Kerékpározás",energyConsumption=3.57,note= "9 km/h sebességnél"),
    EnergyConsumption(activity="Mellúszás",energyConsumption=4.40,note= "1.2 km/h sebességnél"),
    EnergyConsumption(activity="Asztalitenisz",energyConsumption=4.50,note= "-"),
    EnergyConsumption(activity="Korcsolyázás",energyConsumption=5.01,note= "12 km/h sebességnél"),
    EnergyConsumption(activity="Teniszezés",energyConsumption=5.14,note= "-"),
    EnergyConsumption(activity="Lovaglás",energyConsumption=6.70,note= "galoppozásnál"),
    EnergyConsumption(activity="Gimnasztika",energyConsumption=6.71,note= "-"),
    EnergyConsumption(activity="Intenzív úszás",energyConsumption=6.90,note= "-"),
    EnergyConsumption(activity="Kenuzás",energyConsumption=8.10,note= "7.6 km/h sebességnél"),
    EnergyConsumption(activity="Vívás",energyConsumption=8.75,note= "-"),
    EnergyConsumption(activity="Sífutás",energyConsumption=9.00,note= "9 km/h sebességnél"),
    EnergyConsumption(activity="Evezés",energyConsumption=9.30,note= "6 km/h sebességnél"),
    EnergyConsumption(activity="Korcsolyázás",energyConsumption=9.91,note= "21 km/h sebességnél"),
    EnergyConsumption(activity="Futás",energyConsumption=10.07,note= "12 km/h sebességnél"),
    EnergyConsumption(activity="Kerékpározás",energyConsumption=12.00,note= "30 km/h sebességnél"),
    EnergyConsumption(activity="Futás",energyConsumption=12.10,note= "15 km/h sebességnél"),
    EnergyConsumption(activity="Futás",energyConsumption=12.10,note= "15 km/h sebességnél")
]

EnergyConsumption.objects.bulk_create(list1)

input()
