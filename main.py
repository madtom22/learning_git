#Zad1
print('Zad1')
lista = {
    'piekarni': ['chleb', 'bułki', 'pączka'],
    'warzywniaka': ['marchew', 'seler', 'rukolę']
}
things = 0

for shop, stuff in list(lista.items()): # ta pętla przypisuje do pierwszwj zmiennej klucz a do drugiej listę
                                        # przypisaną do klucza
    stuff_up = [] # lista pomocnicza do której przypiszę produkty pisane z dużej litery dla każdego klucza

    for i in range(len(stuff)): # musiałem użyć drugiej pętli do utworzenia list z dużej litery i policzenia produktów
        x = stuff[i] # pobieram produkty z listy i przypisuje je do zmiennej x
        y = x.capitalize() # do zmiennej y przypisuje produkty po zamianie pierwszyj litery na dużą
        stuff_up.append(y) # przypisuje kolejno do listy pomocniczej produkty z dużej litery
        things = things + 1 # zwiększam licznik sumy wszystkich produktów

    print('Idę do', shop.capitalize(), f'i kupuję tu następujące rzeczy: {stuff_up}.')
print(f'W sumie kupuję {things} produktów.')
print('')

#Zad2
print('Zad2')
number_5 = []
cube_5 = []
for x in range(0,101):
    if x % 5 == 0:
        number_5.append(x) # dodaje do listy liczby podzielne przez 5 zgodnie z warunkiem
        cube_5.append(x ** 3) # dodaje do kolejnej listy sześcian liczby spełnijącej warunek
print('Liczba podzielna przez 5 w zakresie od 0 do 100:')
print(number_5)
print('Powyższe liczby podniesione do sześcianu:')
print(cube_5)
