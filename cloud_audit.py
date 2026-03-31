import requests

class CloudAudit:
    def __init__(self, bucket_name):
        self.bucket_url = f"http://{bucket_name}.s3.amazonaws.com"

    def check_exposure(self):
        """
        Checks if a cloud storage bucket is publicly accessible.
        """
        print(f"[*] Auditing Cloud Storage: {self.bucket_url}")
        try:
            response = requests.get(self.bucket_url, timeout=5)
            if response.status_code == 200:
                print(f"[!!!] VULNERABILITY: Public Access Enabled on {self.bucket_url}")
                return True
            else:
                print(f"[+] Bucket is secure (Status: {response.status_code})")
                return False
        except Exception as e:
            print(f"[-] Connection Error: {e}")
            return None

if __name__ == "__main__":
    scanner = CloudAudit("outlaw-test-bucket")
    scanner.check_exposure()
