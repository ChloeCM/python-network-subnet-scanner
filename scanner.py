import subprocess

ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

for ip in ips:
  print("Pinging: ", ip)

  result= subprocess.run(
    ["ping", "-n", "1", ip],
    stdout=subprocess.PIPE,
    text=True
  )

  output = result.stdout

  if "TTL" in output:
    print(ip, " is UP")
  else:
    print(ip, " is DOWN")

  print("-------------------------------")