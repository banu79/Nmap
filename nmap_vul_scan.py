import nmap

def run_nmap_scan(target_ip):
    # Initialize the port scanner
    scanner = nmap.PortScanner()

    # Debug: Print message before scanning
    print(f"Starting scan on {target_ip}...")

    # Run Nmap scan for vulnerabilities on the target IP
    scanner.scan(target_ip, arguments='-sV --script vuln')

    # Debug: Print the raw result
    print(f"Scan result raw output: {scanner.scaninfo()}")

    # Parse and return the scan result
    if target_ip in scanner.all_hosts():
        scan_result = scanner[target_ip]
        return scan_result
    else:
        return "Host seems down or unreachable."

# Test the Nmap vulnerability scan
target_ip = '192.168.29.58'  # Replace with your target IP
scan_result = run_nmap_scan(target_ip)
print(scan_result)