import random

class HydraTelemetry:
    def __init__(self):
        self.metrics = {"CPU": 0, "RAM": 0, "Network_Load": 0}

    def capture_metrics(self):
        """
        Simulates gathering real-time telemetry from a remote security node.
        """
        print("[*] Pulling Telemetry Data...")
        self.metrics["CPU"] = random.randint(10, 85)
        self.metrics["RAM"] = random.randint(200, 4096)
        self.metrics["Network_Load"] = random.randint(1, 1000)
        
        for k, v in self.metrics.items():
            unit = "%" if k == "CPU" else "MB" if k == "RAM" else "Mbps"
            print(f"  [>] {k}: {v}{unit}")
            if v > 80 and k == "CPU":
                print("  [!] WARNING: HIGH LOAD DETECTED")

if __name__ == "__main__":
    eye = HydraTelemetry()
    eye.capture_metrics()
