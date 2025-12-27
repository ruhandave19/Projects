This project is capable of scanning ports and reporting which ones are open.

IMPORTANT NOTE: It is legally allowed to scan ports on localhost only. Scanning external IP addresses without permission can and WILL flag the scanning as a threat. Thus, the code does not allow user input for target and defaults it to localhost. 

To run the code, 3 arguments need to be provided. They are: name of the file, ie, scanner.py, the start port, and the end port.

This scanner was made using synchronous sockets and is not suitable for asynchronous parallel processing like asyncio (due to the connection process on synchronous blocking the program until OS receives a response), and thus can successfully scan less than 1000 ports at once.

To run the code:

```bash
#Open a port locally
python -m http.server 8000
```

Now, in a separate terminal:
```bash
#Clone this repository
git clone https://github.com/ruhandave19/Projects.git
#Navigate into the project folder
cd Projects
cd port_scanner
#Run the script
py scanner.py 7900 8100
```

Example output:
```bash
Port 8000 is open
```