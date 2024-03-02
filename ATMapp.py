
EnesHesap = {
    'Ad' : 'Enes Ünal',
    'HesapNo' : '12345',
    'Bakiye' : 4000,
    'EkHesap' : 2000
}

CuharaHesap = {
    'Ad' : 'Cuhara',
    'HesapNo' : '23456',
    'Bakiye' : 3000,
    'EkHesap' : 1000
}


def ParaCek(hesap, miktar):
    print(f"Merhaba {hesap['Ad']}")

    if (hesap['Bakiye'] >= miktar):
        hesap['Bakiye'] -= miktar
        print("Paranızı alabilirsiniz")
    else:
        toplam = hesap['Bakiye'] + hesap['EkHesap']

        if (toplam >= miktar):
            ekhesapkullanimi = input("ek hesap kullanmak ister misiniz? (e/h)")

            if ekhesapkullanimi == "e":
                kullanilacakMiktar = miktar - hesap['Bakiye']
                hesap['Bakiye'] = 0
                hesap['EkHesap'] -= kullanilacakMiktar
                print("Paranızı alabilirsiniz")
            else:
                print(f"{hesap['HesapNo']} lu hesabınızda {hesap['Bakiye']} vardır.")
        

        else:
            print("Yetersiz Bakiye!!!")

def BakiyeSorgula(hesap):
    print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} tl bulunmaktadır. ekhesabınızda {hesap['EkHesap']} tl vardır. ")





ParaCek(EnesHesap, 3000)
BakiyeSorgula(EnesHesap)
print("*************************")
ParaCek(EnesHesap, 4000)
BakiyeSorgula(EnesHesap)
