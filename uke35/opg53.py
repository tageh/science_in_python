def valuta(euro):
    nok = euro* 10.43
    usd = euro* 1.19
    return (nok, usd)

kr, dollar = valuta(20)

print("nok: ", kr , 'usd: ',dollar)
