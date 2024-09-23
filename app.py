from flask import Flask, jsonify
import nmap

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Chatbot scanner"

@app.route('/scan/<target>')
def scan(target):
    try:
        nmap_path = r"C:\Program Files (x86)\Nmap\nmap.exe"
        scanner = nmap.PortScanner(nmap_search_path=[nmap_path])
        scanner.scan(target, arguments='-sS -sV')
        
        results = {}
        for proto in scanner[target].all_protocols():
            lport = scanner[target][proto].keys()
            results[proto] = {}
            for port in sorted(lport):
                service_info = scanner[target][proto][port]
                results[proto][port] = {
                    "name": service_info['name'],
                    "state": service_info['state'],
                    "version": service_info.get('version', 'N/A')
                }

        return jsonify({"target": target, "results": results})
    except nmap.PortScannerError as e:
        return f"Nmap error: {str(e)}"
    except Exception as e:
        return f"Error scanning {target}: {str(e)}"

@app.route('/nmap_scan', methods=['POST'])
def nmap_scan():
    data = request.json
    ip = data.get('ip')  # Get the IP from the user input

    if not ip:
        return jsonify({"error": "IP address is required"}), 400

    # Running Nmap scan
    nmap_command = f"nmap -sV {ip}"
    scan_output = subprocess.getoutput(nmap_command)  # Run Nmap in the background

    return jsonify({'nmap_result': scan_output})  # Return the scan result

def suggest_exploit(scan_results):
    prompt = f"Based on this Nmap result, suggest possible exploits:\n{scan_results}"
    response = openai.Completion.create(model="gpt-4", prompt=prompt, max_tokens=150)
    
    return response.choices[0].text


if __name__ == '__main__':
    app.run(debug=True)