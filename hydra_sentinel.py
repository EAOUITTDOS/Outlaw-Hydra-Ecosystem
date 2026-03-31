import os
import hashlib
import time

class HydraSentinel:
    def __init__(self, directory_to_watch):
        self.directory = directory_to_watch
        self.file_hashes = {}

    def get_hash(self, filepath):
        return hashlib.md5(open(filepath, 'rb').read()).hexdigest()

    def baseline(self):
        print(f"[*] Establishing Security Baseline for {self.directory}...")
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                path = os.path.join(root, file)
                self.file_hashes[path] = self.get_hash(path)

    def monitor(self):
        print("[!] Sentinel Active. Monitoring for unauthorized changes...")
        while True:
            for path, old_hash in self.file_hashes.items():
                if os.path.exists(path):
                    new_hash = self.get_hash(path)
                    if new_hash != old_hash:
                        print(f"[ALERT] FILE TAMPERING DETECTED: {path}")
                        self.file_hashes[path] = new_hash
            time.sleep(5)

if __name__ == "__main__":
    # Monitor the current directory for testing
    shield = HydraSentinel(".")
    shield.baseline()
    # shield.monitor() # Uncomment to run live
