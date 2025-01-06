import argparse
import os
import subprocess
import sys
import readline
import time
from colorama import Fore
import MD5
import SHA1
import SHA224
import SHA512
import SHA384
import Tool_banner


def main_menu():  
    print(Fore.LIGHTWHITE_EX + "\033[1mAlgorithms available: ")
    print("1) MD5 ")
    print("2) SHA1 ")
    print("3) SHA224 ")
    print("4) SHA384 ")
    print("5) SHA512 ")
    print(Fore.LIGHTRED_EX + "\033[2m99) Exit Hash Cracker ")
    print(Fore.LIGHTBLACK_EX + "=" * 60 + Fore.RESET)

def complete_wordlist_path(text, state):
    """Autocomplete the wordlist file path."""
    directory, partial_file = os.path.split(text)
    directory = directory or '.'  # Default to current directory
    #options = [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith(partial_file)]
    options = [
    f"{f}/" if os.path.isdir(os.path.join(directory, f)) else f
    for f in os.listdir(directory) if f.startswith(partial_file)
]
    options.sort()
    if state < len(options):
        return options[state]
    return None

# Set tab completion for file paths

readline.set_startup_hook(lambda: readline.set_completer(complete_wordlist_path))
readline.parse_and_bind("tab: complete")  # Enable tab completion

def main():
    


    # Create the argument parser
    parser = argparse.ArgumentParser(description="Hash Cracker Tool")

    # Define command line arguments
    parser.add_argument("-md5", action="store_true", help="MD5 hash algorithm")
    parser.add_argument("-sha1", action="store_true", help="SHA1 hash")
    parser.add_argument("-sha224", action="store_true", help="SHA224 hash algorithm")
    parser.add_argument("-sha512", action="store_true", help="SHA512 hash algorithm")
    parser.add_argument("-sha384", action="store_true", help="SHA384 hash algorithm")
    parser.add_argument("--wordlist", type=str, help="Wordlist file path")
    parser.add_argument("-t", type=str, help="Target hash to crack")
    parser.add_argument("--f", type=str, help="Target hash file path with multiple hashes")
    parser.add_argument("--interactive", action="store_true", help="Run the tool in interactive mode")

    # Parse the arguments
    args = parser.parse_args()

    if args.interactive:
        print(Fore.LIGHTBLUE_EX + "Running in interactive mode..." + Fore.RESET)
        time.sleep(3)
        print("No arguments provided. Running with file input mode (provide a file with hashes to crack).")
        os.system("clear" if os.name == "posix" else "cls")
        Tool_banner.main()

        while True:
            main_menu()

            # Validate hash type input
            while True:
                hash_type = input("\033[1;36mWhat's hash type? (1-5 or 99 to exit):\033[0m ")
                if hash_type in ['1', '2', '3', '4', '5', '99']:
                    break
                print("\033[1;31mError: Invalid input. Please enter a number between 1 and 5, or 99 to exit.\033[0m")

            if hash_type == '99':
                print("Exiting Hash Cracker...\nBye!")
                break  # Exit 

            #wordlist location
            while True:
                wordlist_location = input("Enter wordlist location: ")
                try:
                    with open(wordlist_location, encoding='utf-8', errors='ignore') as f:
                        wordlist = f.read()
                    break  # Exit the loop if the wordlist is successfully read
                except FileNotFoundError:
                    print(f"\033[1;31mError: The file at '{wordlist_location}' was not found. Please try again.\033[0m")

            # Check if single hash or a file of hashes
            while True:
                hash_source = input("1) Single hash\n2) File of hashes\nSelect option: ")

                if hash_source == '1':
                    hash_input = input("Enter hash: ")
                    hashes_to_check = [hash_input]
                    break
                elif hash_source == '2':
                    while True:
                        hash_file_location = input("\033[0mEnter hash file location: ")
                        try:
                            with open(hash_file_location, 'r', encoding='utf-8', errors='ignore') as f:
                                hashes_to_check = f.read().splitlines()
                            break  # Exit loop if hash file is successfully read
                        except FileNotFoundError:
                            print(f"\033[1;31mError: The file at '{hash_file_location}' was not found. Please try again.\033[0m")
                    break  # Exit loop 
                else:
                    print("\033[1;31mError: Invalid input. Please enter 1 for a single hash or 2 for a file of hashes.\033[0m")


            # Split the wordlist into individual words
            lists = wordlist.splitlines()
            
            
            if hash_type == '1' and hash_source == '1':
                MD5.MD5(wordlist_location, hash_input,None)
            elif hash_type == '1' and hash_source == '2':
                MD5.MD5(wordlist_location, None,hash_file_location)

            elif hash_type == '2' and hash_source == '1':
                SHA1.SHA1(wordlist_location, hash_input, None)
            elif hash_type == '2' and hash_source == '2':
                SHA1.SHA1(wordlist_location, None, hash_file_location)

            elif hash_type == '3' and hash_source == '1':
                SHA224.SHA224(wordlist_location, hash_input, None)
            elif hash_type == '3' and hash_source == '2':
                SHA224.SHA224(wordlist_location, None, hash_file_location)
            
            elif hash_type == '4' and hash_source == '1':
                SHA384.SHA384(wordlist_location, hashes_to_check)
            elif hash_type == '4' and hash_source == '2':
                SHA384.SHA384(wordlist_location, None,hash_file_location)

            elif hash_type == '5' and hash_source == '1':
                SHA512.SHA512(wordlist_location, hash_input, None)
            elif hash_type == '5' and hash_source == '2':
                SHA512.SHA512(wordlist_location, None, hash_file_location)            
    # Check for hash cracking based on the arguments
    elif args.md5:
        if args.wordlist and args.t:
            MD5.MD5(args.wordlist, args.t,None)
        elif args.f:
            MD5.MD5(args.wordlist, None,args.f)
        else:
            print("Please provide both a wordlist (--wordlist) and a target hash (-t) for MD5.")
    elif args.sha1:
        if args.wordlist and args.t:
            SHA1.SHA1(args.wordlist, args.t, None)
        elif args.f:
            SHA1.SHA1(args.wordlist, None,args.f)
        else:
            print("Please provide both a wordlist (--wordlist) and a target hash (-t) for SHA1.")
    elif args.sha224:
        if args.wordlist and args.t:
            SHA224.SHA224(args.wordlist, args.t, None)
        elif args.f:
            SHA224.SHA224(args.wordlist, None,args.f)
        else:
            print("Please provide both a wordlist (--wordlist) and a target hash (-t) for SHA224.")
    elif args.sha512:
        if args.wordlist and args.t:
            SHA512.SHA512(args.wordlist, args.t, None)
        elif args.f:
            SHA512.SHA512(args.wordlist, None,args.f)
        else:
            print("Please provide both a wordlist (--wordlist) and a target hash (-t) for SHA512.")
    elif args.sha384:
        if args.wordlist and args.t:
            SHA384.SHA384(args.wordlist, args.t, None)
        elif args.f:
            SHA384.SHA384(args.wordlist, None,args.f)
        else:
            print("Please provide both a wordlist (--wordlist) and a target hash (-t) for SHA384.")
    else:
        print("Please specify the hash algorithm (e.g., -md5, -sha1, -sha224, -sha512, -sha384) and the required parameters.")

# Remove the startup hook after completion
readline.set_startup_hook()

if __name__ == "__main__":
    main()
