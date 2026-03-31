import socket
import time
import random

class StealthRecon:
    def __init__(self, target):
        self.target = target

    def low_footprint_scan(self, ports=[80, 443, 22]):
        """
        Uses randomized timing (jitter) to avoid IDS/IPS detection.
        """
        print(f"[*] Initiating Stealth Recon on {self.target}...")
        for port in ports:
            # Add random delay to mimic human behavior
            jitter = random.uniform(1.5, 4.0)
            time.sleep(jitter)
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((self.target, port))
            if result == 0:
                print(f"[!] Port {port} discovered. Status: OPEN.")
            s.close()
        print("[+] Stealth Recon Cycle Complete.")

if __name__ == "__main__":
    ghost = StealthRecon("127.0.0.1")
    ghost.low_footprint_scan()
