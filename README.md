# CYB333 Automated Port Scanner

## CYB 333 Security Automation Project

### Team Members
- Martin Healey
- Edgar Macedo
- Kenny Davis
- Ryan Jay Thomas De Los Santos

## Project Overview

The Automated Port Scanner is a Python-based security automation tool designed to identify open network ports on an approved target system. The project demonstrates how cybersecurity professionals can automate repetitive security assessment tasks using Python.

The scanner allows a user to enter an IP address or hostname and automatically checks a list of commonly used TCP ports. The results are displayed on the screen and saved to a report file for later review.

This project supports the principles of security automation by reducing the time required to perform basic reconnaissance and service discovery activities.

## Features

- Accepts IP addresses and hostnames as input
- Scans common TCP ports
- Detects open and closed ports
- Displays scan results in real time
- Generates a report file
- Basic error handling and input validation

## Technologies Used

- Python 3
- Socket Library
- GitHub
- Visual Studio Code

## Project Structure

CYB333-Automated-Port-Scanner/

├── README.md

├── src/

│   └── port_scanner.py

├── reports/

│   └── scan_results.txt

├── docs/

│   └── project_report.docx

└── screenshots/

## Installation

1. Clone the repository:

git clone https://github.com/healeymd23/CYB333-Automated-Port-Scanner.git

2. Navigate to the project folder.

3. Run the scanner:

python port_scanner.py

## Example Usage

Enter Target IP or Hostname:

127.0.0.1

Choose scan type: Common ports or Custom range.

Common ports examples...

Port 22: Open

Port 80: Closed

Port 443: Open

Scan Complete.

Creates a file with scan results.

## Educational Use Notice

This project was created for educational purposes as part of CYB 333 Security Automation. Scans should only be performed on systems that you own or have explicit permission to test.

## Repository

https://github.com/healeymd23/CYB333-Automated-Port-Scanner
