import numpy as np

names = np.genfromtxt('fornavn.txt', dtype='str')

inp = input("Skriv inn et navn for å sjekke om det ligger i databasen: ")

if inp in names:
    print('Navnet ligger i databasen')
else:
    print('Navnet ligger ikke i databasen')

#sprint(names)