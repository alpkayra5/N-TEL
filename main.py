import phonenumbers
from phonenumbers import carrier,timezone,geocoder

number = input("Telefon Numarasını  Gir: ")

if number.startswith("+"):
    print("Numara Doğru!")
    Numara = phonenumbers.parse(number)
    zaman = timezone.time_zones_for_number(Numara)
    sim_adi = carrier.name_for_number(Numara, "tr")
    bolge = geocoder.description_for_number(Numara, "tr")

    print("Saat Dilimi :", zaman)
    print("Sim adı:", sim_adi)
    print("Yaşadığı Ülke(bölge) :", bolge)

else:
    print("+ülke kodunu kullanarak giriniz.")