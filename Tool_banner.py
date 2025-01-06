import random
import pyfiglet
import pyfiglet
from colorama import Fore, Style, init

banner = pyfiglet.figlet_format("            Hash Cracker")
def banner1():
    print(Fore.CYAN + banner + Fore.RESET)
    print(Fore.CYAN +     "[═══]                 " + Fore.CYAN + "Welcome to Hash Cracker Tool!" + Fore.CYAN + "                            [═══]")
    print(Fore.CYAN +   "[═══]                  Created by: " + Fore.YELLOW + "HUSSEIN RABIO:)" + Fore.CYAN + "                             [═══]")
    print(Fore.CYAN  + "                              Version: " + Fore.MAGENTA + "1.0.0" + Fore.CYAN + "             ")
    print(Fore.CYAN +    "                          Codename: " + Fore.GREEN + "'0xHussein'" + Fore.CYAN + "                \n")
    print(Fore.CYAN +   "[═══]    Follow me on LinkedIn: " + Fore.LIGHTYELLOW_EX + "https://linkedin.com/in/hussein-ibrahim043" + Fore.CYAN + "     [═══]")
    print(Fore.CYAN +   "[═══]        Follow me on Github: " + Fore.YELLOW + "\033[1;33mhttps://github.com/Hussein-Ibrahim043\033[0m" + Fore.CYAN + "        [═══]")
    print(Fore.CYAN + "██" * 42 + Fore.RESET)


def banner2():
    print(Fore.CYAN + """
        ███████╗███████╗███████╗██╗  ██╗ █████╗  ██████╗██╗  ██╗
        ██╔════╝██╔════╝██╔════╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝
        ███████╗█████╗  █████╗  ███████║███████║██║     █████╔╝ 
        ╚════██║██╔══╝  ██╔══╝  ██╔══██║██╔══██║██║     ██╔═██╗ 
        ███████║███████╗███████╗██║  ██║██║  ██║╚██████╗██║  ██╗
        ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
        """ + Fore.RESET)
    print(Fore.CYAN +     "[═══]                 " + Fore.CYAN + "Welcome to Hash Cracker Tool!" + Fore.CYAN + "                            [═══]")
    print(Fore.CYAN +   "[═══]                  Created by: " + Fore.YELLOW + "HUSSEIN RABIO:)" + Fore.CYAN + "                             [═══]")
    print(Fore.CYAN  + "                              Version: " + Fore.MAGENTA + "1.0.0" + Fore.CYAN + "             ")
    print(Fore.CYAN +    "                          Codename: " + Fore.GREEN + "'0xHussein'" + Fore.CYAN + "                \n")
    print(Fore.CYAN +   "[═══]    Follow me on LinkedIn: " + Fore.LIGHTYELLOW_EX + "https://linkedin.com/in/hussein-ibrahim043" + Fore.CYAN + "     [═══]")
    print(Fore.CYAN +   "[═══]        Follow me on Github: " + Fore.YELLOW + "\033[1;33mhttps://github.com/Hussein-Ibrahim043\033[0m" + Fore.CYAN + "        [═══]")
    print(Fore.CYAN + "██" * 42 + Fore.RESET)


def banner3():
    print(Fore.CYAN + """
    ██╗  ██╗ █████╗ ███████╗██╗  ██╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██║  ██║██╔══██╗██╔════╝██║  ██║ ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ███████║███████║███████╗███████║ ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
    ██╔══██║██╔══██║╚════██║██╔══██║ ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ██║  ██║██║  ██║███████║██║  ██║ ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            """ + Fore.RESET)    
    print(Fore.CYAN +     "[═══]                 " + Fore.CYAN + "Welcome to Hash Cracker Tool!" + Fore.CYAN + "                            [═══]")
    print(Fore.CYAN +   "[═══]                  Created by: " + Fore.YELLOW + "HUSSEIN RABIO:)" + Fore.CYAN + "                             [═══]")
    print(Fore.CYAN  + "                              Version: " + Fore.MAGENTA + "1.0.0" + Fore.CYAN + "             ")
    print(Fore.CYAN +    "                          Codename: " + Fore.GREEN + "'0xHussein'" + Fore.CYAN + "                \n")
    print(Fore.CYAN +   "[═══]    Follow me on LinkedIn: " + Fore.LIGHTYELLOW_EX + "https://linkedin.com/in/hussein-ibrahim043" + Fore.CYAN + "     [═══]")
    print(Fore.CYAN +   "[═══]        Follow me on Github: " + Fore.YELLOW + "\033[1;33mhttps://github.com/Hussein-Ibrahim043\033[0m" + Fore.CYAN + "        [═══]")
    print(Fore.CYAN + "██" * 42 + Fore.RESET)
                                                                   
def main():
    banners = [banner1, banner2, banner3]
    random.choice(banners)()  # Randomly call one of the banner functions

if __name__ == "__main__":
    main()
