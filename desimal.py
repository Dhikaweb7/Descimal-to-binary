import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
# Fungsi merubah desimal
# ke binary
# @andhikapratamaputra
print(Fore.BLUE+"=" * 27)
print(Fore.GREEN+"X TKJ 1 | SMK RADEN PAKU")
print(Fore.RED+"RUBAH DESIMAL KE BINER")
print(Fore.BLUE+"=" * 27)

def DecimalToBinary(num):



    if num >= 1:

        DecimalToBinary(num // 2)

    print(num % 2, end = '')

#  masukan angka

if __name__ == '__main__':


  # masukan input (input)

 dec_val  = 1305 # nilai / decimal number


 # manggil fungsi

 DecimalToBinary(dec_val)
