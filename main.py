# Author by Fixsed

import os
import marshal
import colorama
from colorama import Fore, Back, Style
colorama.init()

# Fore.RED
# Style.RESET_ALL


os.system("clear")
print(Fore.RED+"##### TOOLS BY FIXSED #####\n\n"+Style.RESET_ALL)
print(Fore.BLUE+"Kegunaan script ini adalah untuk encrypt script kalian, jadi script kalian gaada di maling >_< \n\n")


file = input(Fore.GREEN+"INPUT FILE >")
baca = open(file, "r").read()
com = compile(baca, "", "exec")

encrypt = marshal.dumps(com)
baru = open("enc_"+str(file), "w")

baru.write("import marshal \n")
baru.write("exec(marshal.loads("+repr(encrypt)+"))")

print("Encrypt berhasil | File di save enc_"+str(file))