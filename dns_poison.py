class DNSPoisoner:
    def __init__(self, target_domain, spoofed_ip):
        self.target = target_domain
        self.spoof = spoofed_ip

    def generate_dns_response(self):
        """
        Creates a mock DNS response to redirect traffic.
        """
        print(f"[*] Crafting DNS Response for {self.target}...")
        print(f"[!] Redirecting {self.target} to {self.spoof}")
        # Logic for injecting a DNS 'A' Record into the cache
        return f"ANSWER: {self.target} is at {self.spoof}"

if __name__ == "__main__":
    redirection = DNSPoisoner("bank.com", "192.168.1.13")
    print(redirection.generate_dns_response())
