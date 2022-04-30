import os
import hashlib
from colorama import Fore


def clear():
    os.system('cls')


def getmd5(fileName):
    hash_md5 = hashlib.md5()
    with open(fileName, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


Menu_banner = f"""
    
        {Fore.LIGHTMAGENTA_EX}Welcome to Cookies FilePumper!
            {Fore.LIGHTBLUE_EX}github.com/callumgm
    
    {Fore.RESET}"""