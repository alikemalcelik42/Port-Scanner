import socket, sys
from threading import Thread

# Port Denetleyici

class PortScanner:
    def __init__(self, target):
        self.target = target
        self.ports =  list(range(1000))
        self.openports = []
        self.Run()

    def ScanPort(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.target, port))
            s.close()
            return True
        except:
            s.close()
            return False

    def Run(self):
        for port in self.ports:
            if self.ScanPort(port):
                self.openports.append(port)
                print("Port {} is open".format(port))
            else:
                print("Port {} is close".format(port))
        print(f"Open ports {self.openports}")

target = input("Enter target: ")
portscanner = PortScanner(target)