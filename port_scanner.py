import socket
import datetime
import pyfiglet
import time

# Common ports that the scanner can check.
common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306]

# Dictionary used to match port numbers with common service names.
services = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    139: 'NetBIOS',
    143: 'IMAP',
    443: 'HTTPS',
    445: 'SMB',
    3306: 'MySQL'
}

# Creates and displays a banner.
banner = pyfiglet.figlet_format('Group 6 \n Project \n "Port Scanner"')
print(banner)

# Print the ethical use warning and approved targets.
print('=' * 55)
print('For educational purposes only.')
print('Only scan systems you own or have permission to test.')
print('=' * 55)

# Record the start time for screenshot verification.
start_time = datetime.datetime.now()
print(f'Scan started at: {start_time}')

# Ask the user to input the target IP address.
target = input('Enter the target IP address or hostname: ')

# Removes the extra space from the target input.
target = target.strip()

print('\nChoose scan type:')
print('1. Common Ports')
print('2. Custom port range')

# Get the user's scan choice.
choice = input('Enter your choice 1 or 2: ').strip()

# Use the common_ports list if the user selects option 1.
if choice == '1':
    ports = common_ports

# Ask user for a custom port range if they select option 2.
elif choice == '2':
    while True:
        try:
            start_port = int(input('Enter the starting port number: '))
            end_port = int(input('Enter the ending port number: '))

            # Check if ports are within valid range.
            if start_port < 1 or end_port > 65535:
                print('Error: Port numbers must be between 1 and 65535.')
                print('Please try again.\n')
                continue

            # Check if the starting port is higher than the ending port.
            if start_port > end_port:
                print('Error: Starting port cannot be greater than ending port.')
                print('Please try again.\n')
                continue

            # If input is valid, create the port range.
            ports = range(start_port, end_port + 1)

            # Break out of the loop oncce valid ports are entered.
            break

        except ValueError:
            # Handles non-number input.
            print('Error: Ports must be entered as numbers.')
            print('Please try again.\n')

# If the user enters the wrong menu option, use common ports by default.
else:
    print('Invalid choice. I will use common ports by default.')
    ports = common_ports

# List used to store scan results.
open_ports = []
closed_ports = []

print(f'\nScanning {target} for open ports...')
print('Please wait...\n')

# loop through each selected port.
for port in ports:
    try:
        # Create a TCPC socket using IPv4.
        # AF_INET means IPv4, and SOCK_STREAM means TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout so the scanner does not wait too long on one port.
        sock.settimeout(0.5)
        
        # connect_ex tries to connect to the target and port.
        # A result of 0 means the port is open.
        result = sock.connect_ex((target, port))

        # Get the common service name for the port, if one is known.
        service = services.get(port, 'Unknown service')

        # Check if port is open or closed.
        if result == 0:
            print(f'[OPEN] Port {port} - {service}')
            open_ports.append(port)

        else:
            print(f'[CLOSED] Port {port} - {service}')
            closed_ports.append(port)

        # CLose the socket after each connection attempt.
        sock.close()

        # Small delay between scans so the scanner is not too aggresive.
        time.sleep(0.2)

    except socket.gaierror:
        # Handles hostname resolution errors.
        print('Error: Hostname could not be resolved.')
        exit()

    except socket.error:
        # Handles general socket connection errors.
        print('Error: Could not connect to target.')
        exit()

# Prints final results.
print('\nScan complete.')
print(f'Total open ports: {len(open_ports)}')
print(f'Total closed ports: {len(closed_ports)}')

# Display open ports if any were found.
if open_ports:
    print('\nOpen ports found:')
    for port in open_ports:
        service = services.get(port, 'Unknown service')
        print(f'Port {port} - {service}')

else:
    print('\nNo open ports found in the selected scan.')

    # Record scan end time.
    end_time = datetime.datetime.now()
    print(f'\nScan ended at: {end_time}')

# Create a report file with the scan results.
timestamp = datetime.datetime.now()
report_name = "scan_report.txt"

with open(report_name, 'w') as report:
    report.write('Group #6 Port Scanner Report\n')
    report.write('=============================\n')
    report.write(f'Target: {target}\n')
    report.write(f'Scan time: {timestamp}\n\n')
    
    # Write open ports to the report.
    if open_ports:
        report.write('Open ports found:\n')
        for port in open_ports:
            service = services.get(port, 'Unknown service')
            report.write(f'Port {port} - {service}\n')
    else:
        report.write('No open ports found.\n')

# Let user know report was created.
print(f'\nReport saved as {report_name}')
