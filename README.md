# Python Subnet Scanner

A simple Python tool that uses ping to check if a host is UP or DOWN.
This project is being built step-by-step to learn network automation fundamentals.

A simple Python-based subnet scanner that pings every usable host in a given subnet and reports whether each IP address is **UP**, **DOWN**, or **timed out**.  
This project was built to learn foundational **network automation** skills, using Python, ICMP (ping), subprocess execution, input validation, and JSON logging.

---

## 🚀 Features

- Scan any IPv4 subnet (e.g., `192.168.1.0/30`)
- Automatically generates all usable host IPs
- Pings each host and checks if it is **UP** or **DOWN**
- Handles:
  - invalid subnets
  - timeouts
  - unreachable hosts
  - unexpected subprocess errors
- Saves all scan results to a structured `results.json` file
- Adds timestamps for:
  - each IP checked
  - beginning and end of the scan
- Beginner friendly, clear, linear Python code
