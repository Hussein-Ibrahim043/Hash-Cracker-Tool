import hashlib

def SHA224(wordlist_path, target_hash=None, hash_file=None):

    try:
        # Read the wordlist file
        with open(wordlist_path, 'r') as file:
            wordlist = file.read().splitlines()

        # Read hashes from file if provided
        if hash_file:
            try:
                with open(hash_file, 'r') as f:
                    hashes_to_check = f.read().splitlines()
            except FileNotFoundError:
                print(f"\033[1;31mError: Hash file '{hash_file}' not found.\033[0m")
                return
        elif target_hash:
            hashes_to_check = [target_hash]
        else:
            print("\033[1;31mError: No hash or hash file provided.\033[0m")
            return

        # Track found hashes
        found_hashes = []

        # Iterate over each word in the wordlist
        for word in wordlist:
            # Generate MD5 hash of the word
            hashed = hashlib.sha224(word.encode('utf-8')).hexdigest()

            # Check if the hash matches any of the provided hashes
            if hashed in hashes_to_check:
                print(f"\033[1;32m{hashed}  {word}\033[0m")
                found_hashes.append({'word': word, 'hashed': hashed})

                # Remove the found hash to optimize further checks
                hashes_to_check.remove(hashed)

        for hash in hashes_to_check:
            print(f"\033[1;31m{hash}  NOT FOUND\033[0m")

        return found_hashes
       
    except FileNotFoundError:
        print(f"\033[1;31mError: Wordlist file '{wordlist_path}' not found.\033[0m")

