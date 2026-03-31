import base64

class PayloadHydra:
    def __init__(self, raw_command):
        self.raw_command = raw_command

    def obfuscate_payload(self):
        """
        Encodes payloads to bypass basic string-matching security filters.
        """
        encoded = base64.b64encode(self.raw_command.encode()).decode()
        print(f"[*] Obfuscated Payload Generated: {encoded}")
        return encoded

    def generate_stager(self):
        payload = self.obfuscate_payload()
        stager = f"python3 -c 'import base64,os;os.system(base64.b64decode(\"{payload}\").decode())'"
        print(f"[+] Security Stager Ready: \n{stager}")
        return stager

if __name__ == "__main__":
    factory = PayloadHydra("echo 'Hydra Security Audit Active'")
    factory.generate_stager()
