import hashlib
import requests

def is_pwned(password: str) -> bool:
    # Return True if the password appears in known breaches (HIBP)
    # Hash locally (required by HIBP)
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    # Query the k-Anonymity range endpoint
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    headers = {
        "Add-Padding": "true",             # privacy: normalize response size
        "User-Agent": "PassWchecker/mini", # polite header
    }
    resp = requests.get(url, headers=headers, timeout=10) 
    resp.raise_for_status() # Raise an error for bad responses

    # Look for our suffix in the results (format: "SUFFIX:COUNT")
    for line in resp.text.splitlines():
        parts = line.split(":")
        if len(parts) == 2 and parts[0].upper() == suffix:
            print(f"Password found {parts[1]} times in breaches.")
            return int(parts[1]) > 0 # Return True if found
    print("Password NOT found in a data breach.") # Print if not found
    return False# Return False if not found