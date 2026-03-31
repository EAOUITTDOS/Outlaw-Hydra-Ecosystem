import hashlib

class HashCracker:
    def __init__(self, target_hash, algorithm="md5"):
        self.target = target_hash
        self.algo = algorithm

    def crack(self, wordlist=["123456", "password", "admin", "outlaw"]):
        print(f"[*] Attempting to crack {self.algo} hash: {self.target}")
        for word in wordlist:
            # Generate hash of the word to compare
            test_hash = hashlib.md5(word.encode()).hexdigest()
            if test_hash == self.target:
                print(f"[!!!] HASH CRACKED: {word}")
                return word
        print("[-] Password not found in wordlist.")
        return None

if __name__ == "__main__":
    # MD5 hash for 'password'
    target = "5f4dcc3b5aa765d61d8327deb882cf99"
    breaker = HashCracker(target)
    breaker.crack()
