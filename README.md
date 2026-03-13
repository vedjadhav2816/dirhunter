# DirHunter

DirHunter is a Python-based web reconnaissance tool designed to discover hidden directories and files on web servers using wordlists.

The tool was built to understand how directory brute-force scanners work internally and to practice ethical hacking automation techniques.

## Features

* High-speed asynchronous scanning
* Custom wordlist support
* Extension brute forcing (.php, .html, .js)
* Live scanning progress bar
* JSON result reporting
* Automatic HTML scan report
* Proxy support for testing with Burp Suite
* Lightweight CLI interface

## Example Usage

python3 dirhunter.py -u https://target.com -w wordlists/common.txt

## Output

DirHunter generates:

* report.json → structured scan results
* report.html → visual scan report

## Project Structure

dirhunter/
│
├── dirhunter.py
├── README.md
├── wordlists/
│   └── common.txt
├── report.json
└── report.html

## Learning Goals

This project helped explore:

* Python networking
* asynchronous programming
* CLI tool development
* web reconnaissance techniques
* security automation

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.
Do not scan systems without permission.

## Future Improvements

* smarter 404 detection
* subdomain discovery
* automatic wordlist expansion
* faster scanning engine
* vulnerability pattern detection

