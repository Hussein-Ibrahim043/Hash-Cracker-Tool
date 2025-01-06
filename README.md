# Hash-Cracker-Tool
## Overview

Welcome to the **Hash Cracker Tool**! This tool is designed for educational purposes, showcasing a simple Python-based hash cracking interface. It includes a variety of features, such as customizable banners and a clean user interface, which enhances the tool's overall functionality.
This project is a powerful and flexible command-line tool for cracking various hash types using wordlists. It supports multiple hash algorithms, including MD5, SHA1, SHA224, SHA384, and SHA512. The tool offers both interactive and command-line modes, providing an efficient and user-friendly experience.


---

## ✨Features
- Supports multiple hash algorithms:
  - **MD5**
  - **SHA1**
  - **SHA224**
  - **SHA384**
  - **SHA512**
- Two operation modes:
  - **Interactive Mode**: User-friendly mode for manual inputs.
  - **CLI Mode**: Efficient for automation and scripting.
- Wordlist-based cracking.
- Ability to handle single hashes or files containing multiple hashes.
- Auto-completion for file paths using `readline`.


- **Interactive Mode**: Run the tool in interactive mode using the --interactive flag:
          `python hash_cracker.py --interactive`
- **CLI Mode**
  `python hash_cracker.py [OPTIONS]`
-**Available Arguments:**
  --interactive: Runs the tool in interactive mode.
  -md5: Crack MD5 hash.
  -sha1: Crack SHA1 hash.
  -sha224: Crack SHA224 hash.
  -sha384: Crack SHA384 hash.
  -sha512: Crack SHA512 hash.
  --wordlist [file]: Specify the wordlist file.
  -t [hash]: Specify the target hash.
  --f [file]: Specify a file containing multiple hashes.

  `python hash_cracker.py -md5 --wordlist rockyou.txt -t 5f4dcc3b5aa765d61d8327deb882cf99`


Additionally, you need to specify:
`--wordlist` for the wordlist file.
`-t` for the target hash.
`--f` for a file containing multiple hashes.

---

## Supported Hash Algorithms
  MD5: `-md5`
  SHA1: `-sha1`
  SHA224: `-sha224`
  SHA384: `-sha384`
  SHA512: `-sha512`
  

## 🛠️ Requirements
- Python 3.13.1 or later
- Required libraries:
  - `argparse`
  - `colorama`
  - `hashlib`
  - `readline`
Install the required dependencies:

   `pip install -r requirements.txt`

---

## Installation

1. Clone the Repository:

   Clone the GitHub repository to your local machine:

   ```bash
   `git clone https://github.com/Hussein-Ibrahim043/Hash-Cracker-Tool.git`

2. Run the provided install.sh script to install the tool and set up an alias for easy usage.

   `cd Hash-Cracker-Tool`

4. Run install.sh :

   `sudo bash install.sh`
   
The alias `hashcracker` will be created for the tool.

---

## 🚀 How to Use
1. Interactive Mode:
   Launch the script from the terminal:
     - `hashcracker --interactive`
2. Command-Line Arguments:
   - `hashcracker -md5 --wordlist rockyou.txt -t 5f4dcc3b5aa765d61d8327deb882cf99`
   **Command-Line Options**:
     -`md5`: Crack an MD5 hash.
     -`sha1`: Crack a SHA1 hash.
     -`sha224`: Crack a SHA224 hash.
     -`sha384`: Crack a SHA384 hash.
     -`sha512`: Crack a SHA512 hash.
     --`wordlist`: Specify the path to the wordlist.
     `-t`: Provide a single target hash.
     --f: Provide a file containing multiple hashes.
**Examples**:
          1. Crack a single MD5 hash:
               `hashcracker -md5 --wordlist wordlist.txt -t d41d8cd98f00b204e9800998ecf8427e`
          2.Crack multiple SHA1 hashes from a file:
               `hashcracker -sha1 --wordlist wordlist.txt --f hashes.txt`
          
---

## 🛡️ Troubleshooting

**File Not Found Error** : Ensure the wordlist file or hash file exists at the specified location.
**Invalid Hash** : Make sure the provided hash is of the correct type (MD5, SHA1, etc.).

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Author

- GitHub (https://github.com/Hussein-Ibrahim043)
- LinkedIn (https://linkedin.com/in/hussein-ibrahim043)
