# Author by Fixsed

import os
import marshal
import colorama
from colorama import Fore, Back, Style
colorama.init()

# Fore.RED
# Style.RESET_ALL


os.system("clear")
print(Fore.RED+"_-_-_-_-_-_-_-_-_-_-_-__-_--_-__-_-_-__-_-_--_-_ _-_-_-_-_-_-_-_-_-_-_-__-_--_-__-_-_-__-_-_--_-_SCRIPT BY FIXSED >_< _-_-_-_-_-_-_-_-_-_-_-__-_--_-__-_-_-__-_-_--_-_ \n\n"+Style.RESET_ALL)
print(Fore.RED+"Kegunaan script ini adalah untuk encrypt script kalian, jadi script kalian gaada di maling >_< \n\n")


file = input(Fore.GREEN+"INPUT FILE >")
baca = open(file, "r").read()
com = compile(baca, "", "exec")

encrypt = marshal.dumbs(com)
baru = open("enc_"+str(file), "w")

baru.write("import marshal \n")
baru.write("exec(marshal.loads("+repr(encpypt)+"))")

print("Encrypt berhasil | File di save enc_"+str(file))