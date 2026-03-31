import requests

class APIFuzzer:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.payloads = ["' OR 1=1--", "<script>alert(1)</script>", "../../../etc/passwd", "{'admin': true}"]

    def fuzz_endpoint(self):
        print(f"[*] Fuzzing API Endpoint: {self.endpoint}")
        for p in self.payloads:
            print(f"  [>] Testing payload: {p}")
            # Mocking a POST request with the malicious payload
            response = requests.post(self.endpoint, data={"input": p})
            if response.status_code == 500:
                print(f"  [!] Potential Server Error / Vulnerability Found with payload: {p}")
            elif "root:" in response.text:
                print(f"  [!!!] CRITICAL: File Disclosure detected!")

if __name__ == "__main__":
    fuzzer = APIFuzzer("https://api.outlawlabs.com/v1/test")
    # fuzzer.fuzz_endpoint() # Uncomment to run live
  
