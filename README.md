# Decimal convert to binary
Convert Decimal number to binary number with Python🐍

<hr>

Decimal to binary conversion program with ``Python``, I made this for a computer system lesson in the number system section in my school <a href="https://dhikaweb7.github.io">SMK RADEN PAKU</a>

> Running in terminal (for Linux and Mac) or cmd (for Windows) 

> Indonesian language 🇮🇩

# Preview

![Screenshot_20220730-063742](https://user-images.githubusercontent.com/107765982/181860789-5a1ac69c-6e09-4f3c-b9c9-018ed4d74f2b.png)

Requirement

 - Python3
 - Colorama (Optional but my prefer about the colors😅)

```Python

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


  # masukan input

 dec_val  = 1305 # contoh masukan nilai / example of Decimal number


 # manggil fungsi

 DecimalToBinary(dec_val)

```

# Install

Install Python3

```bash

apt-get-install Python3

```

Install Colorama

```bash

pip install colorama

```

Cloning repo 

```url

git clone https://github.com/Dhikaweb7/Descimal-to-binary
```

<hr>


# Number of System

``BINARY``

``DECIMAL``

``HEXADECIMAL``

``OKTAL``
