import subprocess
import ipaddress

# Ask user for a subnet
subnet = input("Enter a subnet (e.g. 192.168.1.0/30): ")

# Convert the text into a network object
network = ipaddress.ip_network(subnet, strict=False)

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
        print(ip_str, "is UP")
    else:
        print(ip_str, "is DOWN")

    print("----------------------")