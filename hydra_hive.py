import time

class HydraHive:
    def __init__(self):
        self.nodes = ["Node-Alpha", "Node-Bravo", "Node-Delta"]
        self.active_tasks = {}

    def assign_task(self, node, task):
        """
        Assigns specific security tasks to distributed Hydra nodes.
        """
        if node in self.nodes:
            print(f"[*] Dispatching task '{task}' to {node}...")
            self.active_tasks[node] = task
            return True
        return False

    def get_status(self):
        print("\n--- Hydra Hive: Node Status Report ---")
        for node in self.nodes:
            status = self.active_tasks.get(node, "IDLE")
            print(f"[+] {node}: {status}")
        print("---------------------------------------\n")

if __name__ == "__main__":
    hive = HydraHive()
    hive.assign_task("Node-Alpha", "Massive Log Parsing")
    hive.assign_task("Node-Bravo", "Port Audit: 192.168.1.50")
    hive.get_status()
