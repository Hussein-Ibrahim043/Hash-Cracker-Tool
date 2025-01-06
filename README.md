# Hash-Cracker-Tool
## Overview

Welcome to the **Hash Cracker Tool**! This tool is designed for educational purposes, showcasing a simple Python-based hash cracking interface. It includes a variety of features, such as customizable banners and a clean user interface, which enhances the tool's overall functionality.
This project is a powerful and flexible command-line tool for cracking various hash types using wordlists. It supports multiple hash algorithms, including MD5, SHA1, SHA224, SHA384, and SHA512. The tool offers both interactive and command-line modes, providing an efficient and user-friendly experience.


---

## ✨Features

- **Random Banner Display**: The tool will display one of three random banners every time it's run, providing a dynamic and personalized experience.
- **Colorful Output**: Color-coded output for better readability and a pleasant user experience.
- **Customizable Banners**: The banners are displayed using ASCII art, allowing for different styles and customization options.
- **User Information**: Displays creator information, version, and social media links for easy access.
- **Interactive Mode**:When the script is run without arguments, it enters interactive mode, where the user can:
          Choose the hash algorithm (MD5, SHA1, SHA224, SHA384, or SHA512).
          Provide a wordlist file location.
          Specify whether to crack a single hash or multiple hashes from a file.
  
- **Command-line Mode**
You can also use the tool in command-line mode by specifying flags:

-md5 to crack MD5 hashes.
-sha1 to crack SHA1 hashes.
-sha224 to crack SHA224 hashes.
-sha512 to crack SHA512 hashes.
-sha384 to crack SHA384 hashes.

Additionally, you need to specify:
--wordlist for the wordlist file.
-t for the target hash.
--f for a file containing multiple hashes.
---
## Supported Hash Algorithms
  MD5: -md5
  SHA1: -sha1
  SHA224: -sha224
  SHA384: -sha384
  SHA512: -sha512
  

## 🛠️ Requirements

- Python 3.13.1 or later
- Required libraries:
  - `argparse`
  - `colorama`
  - `hashlib`
  - `readline`

---

## Installation

1. Clone the Repository**:

   Clone the GitHub repository to your local machine:

   ```bash
   git clone https://github.com/Hussein-Ibrahim043/Hash-Cracker-Tool.git

3. Navigate to the project directory:

   cd Hash-Cracker-Tool

4. Install the required dependencies:

   pip install -r requirements.txt

---

## 🚀 How to Use
1. Run the Python Script:
   Launch the script from the terminal:
     - python hash_cracker_tool.py
   Or, if you've set up the alias:
     - hashcrack
2. Provide IP Addresses:
   - You’ll be prompted to enter the Source IP and Destination IP.
- The script will send an ICMP packet from the source to the destination and log the results.
3. Sample Output:
  After you input the IP addresses, the script will:
    - Send the ICMP packet.
    - Capture and log the response (if received).
    - Store detailed logs of sent and received packets in packet_logs.txt.

---

## 📝 Example Log (packet_logs.txt)



---

## 🔧 Logging and Debugging
- Logs are saved automatically in `packet_logs.txt` with timestamps.
- These logs include both sent and received packet details as well as any errors encountered during packet transmission.

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

- Hussein Ibrahim (https://github.com/Hussein-Ibrahim043)
