#Kupno samochodu
#Program oblicza ile będzie kosztował samochód wraz z wszystkimi opłatami

suma = int(input("Wprowadź kwotę samochodu a dowiesz się ile z tego było podatku "))

vat = suma * 0.23
serwis = suma * 0.1
prowizja = suma * 0.05
rejstracja = 100
calosc = suma - (vat + serwis + prowizja + rejstracja)
calosc_2 = vat + serwis + prowizja + rejstracja
print("\nW kwocie zakupu samochodu mieszczą się jeszcze takie opłaty jak \nVAT", vat,
      "\nSerwis", serwis, "\nProwizja sprzedawcy", prowizja, "\noraz koszt rejstracji w urzędzie", rejstracja)


print("Za sam samochód zapłaciłbyś ", calosc, "a tak na opłaty idzie ", calosc_2, "\nFajnie, co nie?")

input("Aby zakończyć naciśij enter")
