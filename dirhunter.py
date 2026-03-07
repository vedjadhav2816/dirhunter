import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from fake_useragent import UserAgent
import json

results = []
ua = UserAgent()

def scan(url, word, extensions):

    word = word.strip()

    paths = [word]

    for ext in extensions:
        paths.append(word + ext)

    for path in paths:

        target = f"{url}/{path}"

        headers = {
            "User-Agent": ua.random
        }

        try:

            r = requests.get(target, headers=headers, timeout=5)

            if r.status_code in [200,301,302,403]:

                print(f"[+] {target} | {r.status_code}")

                results.append({
                    "url": target,
                    "status": r.status_code
                })

        except:
            pass


def main():

    parser = argparse.ArgumentParser(description="DirHunter v2")

    parser.add_argument("-u","--url", required=True)
    parser.add_argument("-w","--wordlist", required=True)
    parser.add_argument("-t","--threads", type=int, default=20)
    parser.add_argument("-e","--extensions", default=".php,.html,.js")

    args = parser.parse_args()

    extensions = args.extensions.split(",")

    with open(args.wordlist,"r") as f:
        words = f.readlines()

    print("\nStarting DirHunter Scan...\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:

        for word in tqdm(words):

            executor.submit(scan,args.url,word,extensions)

    with open("report.json","w") as f:

        json.dump(results,f,indent=4)

    print("\nScan Complete")
    print("Report saved to report.json")


if __name__ == "__main__":
    main()
