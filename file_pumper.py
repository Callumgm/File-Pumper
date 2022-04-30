from colorama import Fore
from util.common import *

clear()

def main():
    clear()
    print(Menu_banner)
    filePath = str(input(f"{Fore.LIGHTCYAN_EX}Enter path to file u wish to pump {Fore.LIGHTYELLOW_EX}>> {Fore.RESET}"))
    pumpSize = int(input(f"{Fore.LIGHTCYAN_EX}Enter pump amount {Fore.LIGHTYELLOW_EX}>> {Fore.RESET}"))
    unitType = str(input(f"{Fore.LIGHTCYAN_EX}Enter unit type {Fore.RESET}({Fore.LIGHTGREEN_EX}kb{Fore.RESET}/{Fore.LIGHTGREEN_EX}mb{Fore.RESET}) {Fore.LIGHTYELLOW_EX}>> {Fore.RESET}"))

    oldMD5 = getmd5(filePath)
    pumpFile = open(filePath, 'ab')

    bytesFileSize = 0

    if (unitType == "kb"):
        bytesFileSize = pumpSize * 1024

    elif (unitType == "mb"):
        bytesFileSize = pumpSize * pow(1024, 2)

    else:
        clear()
        print(f"{Fore.RED}Invalid unit type! {Fore.RESET}")
        input(f"\n{Fore.YELLOW}Press enter to continue. . .{Fore.RESET}")
        main()

    buffer = 256
    for i in range(int(bytesFileSize/buffer)):
        pumpFile.write((b"0" * buffer))

    newMD5 = getmd5(filePath)

    clear()
    print(f"{Fore.GREEN}File Pumping Completed!{Fore.RESET}")
    input(f"\n{Fore.YELLOW}Press enter to continue. . .{Fore.RESET}")
    main()

    pumpFile.close()


main()

