import subprocess
import ipaddress
import json
from datetime import datetime

# Ask user for a subnet
subnet = input("Enter a subnet (e.g. 192.168.1.0/30): ")

# Convert the text into a network object
network = ipaddress.ip_network(subnet, strict=False)

# New list for storing the results
results = []

# Overall start time
scan_start = datetime.now().isoformat(timespec="seconds")

# Loop through all usable IPs in the subnet
for ip in network.hosts():
    ip_str = str(ip)
    print("Pinging:", ip_str)

    result = subprocess.run(
        ["ping", "-n", "1", ip_str],
        stdout=subprocess.PIPE,
        text=True
    )

    output = result.stdout

    if "TTL" in output:
        status = "UP"
    else:
        status = "DOWN"

    print(ip_str, " is ", status)
    print("----------------------")

    # Timestamp for each IP scanned
    timestamp = datetime.now().isoformat(timespec="seconds")

    # Store results as an object
    results.append({
        "ip: ": ip_str, 
        "status ": status,
        "timestamp: ": timestamp
        })
    
# JSON structure
output_data = {
    "subnet: ": subnet,
    "scan_started_at: ": scan_start,
    "scan_finished_at: ": datetime.now().isoformat(timespec="seconds"),
    "results :": results
}

    # Save to JSON file
with open("results.json", "w") as file:
    json.dump(results, file, indent=4)

print("Results saved to results.json")