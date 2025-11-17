import subprocess

ip = "8.8.8.8"

print("Pinging IP: ", ip)

# Run a single ping
result = subprocess.run(
  ["ping", "-n", "1", ip],
  stdout=subprocess.PIPE,
  text=True
)

output = result.stdout

# Check if ping succeeded
if "TTL" in output:
  print("Host is Up")
else:
  print("Host is down")


# import subprocess 
# import json
# import ipaddress

# def ping_ip(ip):
#   # This runs a single ping command
#   try:
#     result = subprocess.run(
#       ["ping", "-n", "1", "-w", "200", ip],
#       stdout=subprocess.PIPE,
#       stderr=subprocess.PIPE,
#       text=True
#     )
#     # If "TTL" appears in the output, the host is up and running
#     return "TTL" in result.stdout
#   except Exception:
#     return False
  
# def scan_subnet(cidr):
#   network = ipaddress.ip_network(cidr, strict=False)
#   results = []

#   print(f"Scanning subnet: {cidr}")

#   for ip in network.hosts():
#         ip_str = str(ip)
#         print(f"Pinging {ip_str}...")
#         is_up = ping_ip(ip_str)

#         status = "UP" if is_up else "DOWN"
#         print(f"{ip_str} is {status}")

#         results.append({"ip": ip_str, "status": status})

#   return {"subnet": cidr, "hosts": results}


# def save_results(results):
#     with open("results.json", "w") as f:
#         json.dump(results, f, indent=4)


# if __name__ == "__main__":
#     subnet = input("Enter subnet (e.g., 192.168.1.0/29): ")
#     scan_output = scan_subnet(subnet)
#     save_results(scan_output)
#     print("Scan complete. Results saved to results.json.") 