import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

init(autoreset=True)

found_urls = []

def scan(url, word):
    word = word.strip()
    target = f"{url}/{word}"

    try:
        r = requests.get(target, timeout=5)

        if r.status_code in [200,301,302,403]:
            print(Fore.GREEN + f"[+] Found: {target} | {r.status_code}")
            found_urls.append(target)
        else:
            print(Fore.RED + f"[-] Not Found: {target}")

    except:
        pass


def main():

    parser = argparse.ArgumentParser(description="DirHunter Advanced Scanner")
    parser.add_argument("-u","--url",required=True)
    parser.add_argument("-w","--wordlist",required=True)
    parser.add_argument("-t","--threads",type=int,default=10)

    args = parser.parse_args()

    with open(args.wordlist,"r") as f:
        words = f.readlines()

    print(Fore.CYAN + f"\nStarting scan on {args.url}\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for word in words:
            executor.submit(scan,args.url,word)

    if found_urls:
        with open("results.txt","w") as f:
            for url in found_urls:
                f.write(url+"\n")

        print(Fore.YELLOW + "\nResults saved in results.txt")

if __name__ == "__main__":
    main()
