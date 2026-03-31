import base64
import json

class JWTHydra:
    def __init__(self, token):
        self.token = token

    def decode_token(self):
        """
        Decodes the header and payload of a JWT without the secret.
        """
        try:
            parts = self.token.split('.')
            header = base64.b64decode(parts[0] + '==').decode()
            payload = base64.b64decode(parts[1] + '==').decode()
            print(f"[*] JWT Header: {header}")
            print(f"[*] JWT Payload: {payload}")
            
            data = json.loads(payload)
            if data.get('admin') == False:
                print("[*] Suggested exploit: Attempt 'None' algorithm or Flip admin bit.")
        except Exception as e:
            print(f"[-] Error decoding token: {e}")

if __name__ == "__main__":
    # Sample encoded JWT (Header.Payload.Signature)
    sample_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiamVzc2UiLCJhZG1pbiI6ZmFsc2V9.signature"
    cracker = JWTHydra(sample_jwt)
    cracker.decode_token()
