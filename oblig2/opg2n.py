import numpy as np

names = np.genfromtxt('fornavn.txt', dtype='str')

navn = input("Skriv inn et navn: ")

if navn in names:
    print("Navnet ligger i databasen")
if not navn in names:
    print("Navnet ligger ikke i databasen")
