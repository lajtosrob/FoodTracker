
from .models import EnergyConsumption


data = [
    {"activity":"Fekvés","energyConsumption":"1.10","note": "-"},
    {"activity":"Állás","energyConsumption":"1.58","note": "-"},
    {"activity":"Gépkocsivezetés","energyConsumption":"1.60","note": "-"},
    {"activity":"Séta","energyConsumption":"2.75","note": "3 km/h sebességnél"},
    {"activity":"Gyaloglás","energyConsumption":"3.70","note": "6 km/h sebességnél"},
    {"activity":"Háztartási munka","energyConsumption":"3.43","note": "-"},
    {"activity":"Kerékpározás","energyConsumption":"3.57","note": "9 km/h sebességnél"},
    {"activity":"Mellúszás","energyConsumption":"4.40","note": "1.2 km/h sebességnél"},
    {"activity":"Asztalitenisz","energyConsumption":"4.50","note": "-"},
    {"activity":"Korcsolyázás","energyConsumption":"5.01","note": "12 km/h sebességnél"},
    {"activity":"Teniszezés","energyConsumption":"5.14","note": "-"},
    {"activity":"Lovaglás","energyConsumption":"6.70","note": "galoppozásnál"},
    {"activity":"Gimnasztika","energyConsumption":"6.71","note": "-"},
    {"activity":"Intenzív úszás","energyConsumption":"6.90","note": "-"},
    {"activity":"Kenuzás","energyConsumption":"8.10","note": "7.6 km/h sebességnél"},
    {"activity":"Vívás","energyConsumption":"8.75","note": "-"},
    {"activity":"Sífutás","energyConsumption":"9.00","note": "9 km/h sebességnél"},
    {"activity":"Evezés","energyConsumption":"9.30","note": "6 km/h sebességnél"},
    {"activity":"Korcsolyázás","energyConsumption":"9.91","note": "21 km/h sebességnél"},
    {"activity":"Futás","energyConsumption":"10.07","note": "12 km/h sebességnél"},
    {"activity":"Kerékpározás","energyConsumption":"12.00","note": "30 km/h sebességnél"},
    {"activity":"Futás","energyConsumption":"12.10","note": "15 km/h sebességnél"},
    {"activity":"Futás","energyConsumption":"12.10","note": "15 km/h sebességnél"}
    
]

for entry in data:
    EnergyConsumption.objects.create(**entry)