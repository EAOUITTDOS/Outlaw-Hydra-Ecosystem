import base64

class HydraVault:
    def __init__(self, master_key):
        self.key = master_key

    def encrypt_data(self, raw_text):
        """
        Simulates AES-256 encryption for sensitive Hydra credentials.
        """
        print(f"[*] Encrypting sensitive data with Master Key...")
        # Mocking an encryption shift for demonstration
        encoded = base64.b64encode(raw_text.encode()).decode()
        return f"HYDRA_ENC_{encoded}"

    def decrypt_data(self, encrypted_text):
        if not encrypted_text.startswith("HYDRA_ENC_"):
            return "ERROR: INVALID ENCRYPTION FORMAT"
        raw_part = encrypted_text.replace("HYDRA_ENC_", "")
        return base64.b64decode(raw_part).decode()

if __name__ == "__main__":
    vault = HydraVault("OUTLAW_SECRET_KEY")
    secret = "API_KEY_55928374"
    enc = vault.encrypt_data(secret)
    print(f"[+] Encrypted: {enc}")
    print(f"[+] Decrypted: {vault.decrypt_data(enc)}")
