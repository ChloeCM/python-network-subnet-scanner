# Python Subnet Scanner

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

---

## 📄 Example Output (results.json)

```json
{
  "subnet": "192.168.1.0/30",
  "scan_started_at": "2025-11-13T20:10:55",
  "scan_finished_at": "2025-11-13T20:10:57",
  "results": [
    {
      "ip": "192.168.1.1",
      "status": "DOWN",
      "timestamp": "2025-11-13T20:10:56"
    },
    {
      "ip": "192.168.1.2",
      "status": "UP",
      "timestamp": "2025-11-13T20:10:57"
    }
  ]
}
```

---

## ▶️ How to Run

1. Install Python 3

2. Clone this repository

  ```bash
     git clone https://github.com/ChloeCM/python-network-subnet-scanner.git
     cd python-network-subnet-scanner
  ```

3. Run the scanner

   ```bash
   python scanner.py
   ```

4. Enter a subnet when prompted, e.g. 192.168.1.0/29

5. View results in: results.json

---

🧠 How It Works (Simple Explanation)

- The user enters a subnet such as 192.168.1.0/30.
- Python validates it using the built-in ipaddress module.
- The script generates a list of usable host addresses (skips network + broadcast).
- Each host is pinged once using:
-   a 2-second Windows ping timeout (-w 2000)
-   a 3-second Python subprocess timeout (timeout=3)
- The script checks the ping output for "TTL" to determine if the host is UP.
- All scan results are stored in results.json with timestamps.
- This mirrors how simple network monitoring tools operate.

---

🛠️ Skills Demonstrated

- Python scripting
- Calling system commands with subprocess
- ICMP ping automation
- Error handling
- Input validation
- Working with IPv4 subnets (ipaddress module)
- Creating structured JSON logs
- Timestamp formatting
- Writing clear, maintainable automation code

---

📌 Future Improvements (Optional)

- Multi-threaded scanning for speed
- Saving logs into timestamped files in a logs or folder
- Retry logic (ping an IP multiple times)

