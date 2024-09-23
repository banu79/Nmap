from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Endpoint for Nmap scanning
@app.route('/nmap_scan', methods=['POST'])
def nmap_scan():
    data = request.json
    ip = data.get('ip')

    # Running Nmap scan
    nmap_command = f"nmap -sV {ip}"
    scan_output = subprocess.getoutput(nmap_command)

    # Return the raw scan result to chatbot
    return jsonify({'nmap_result': scan_output})

if __name__ == '__main__':
    app.run(debug=True)