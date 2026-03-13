import asyncio
import aiohttp
import argparse
from tqdm import tqdm
import json
from datetime import datetime

results = []

async def scan(session, url, word, extensions, proxy):

    word = word.strip()

    paths = [word]

    for ext in extensions:
        paths.append(word + ext)

    for path in paths:

        target = f"{url}/{path}"

        try:

            async with session.get(target, proxy=proxy) as response:

                if response.status in [200,301,302,403]:

                    print(f"[+] {target} | {response.status}")

                    results.append({
                        "url": target,
                        "status": response.status
                    })

        except:
            pass


async def main():

    parser = argparse.ArgumentParser(description="DirHunter v3")

    parser.add_argument("-u","--url",required=True)
    parser.add_argument("-w","--wordlist",required=True)
    parser.add_argument("-e","--extensions",default=".php,.html,.js")
    parser.add_argument("-p","--proxy",default=None)

    args = parser.parse_args()

    extensions = args.extensions.split(",")

    with open(args.wordlist) as f:
        words = f.readlines()

    connector = aiohttp.TCPConnector(limit=100)

    async with aiohttp.ClientSession(connector=connector) as session:

        tasks = []

        for word in words:

            tasks.append(scan(session,args.url,word,extensions,args.proxy))

        for task in tqdm(asyncio.as_completed(tasks), total=len(tasks)):

            await task

    with open("report.json","w") as f:

        json.dump(results,f,indent=4)

    generate_html()


def generate_html():

    html = f"""
    <html>
    <head>
    <title>DirHunter Report</title>
    </head>
    <body>
    <h1>DirHunter Scan Report</h1>
    <p>Date: {datetime.now()}</p>
    <table border="1">
    <tr><th>URL</th><th>Status</th></tr>
    """

    for r in results:

        html += f"<tr><td>{r['url']}</td><td>{r['status']}</td></tr>"

    html += "</table></body></html>"

    with open("report.html","w") as f:

        f.write(html)

    print("\nHTML report saved as report.html")


if __name__ == "__main__":

    asyncio.run(main())
