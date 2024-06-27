import requests
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp
async def download_aiohttp(url):
    log_file = url.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            with open(log_file,'w') as f:
                f.write(text)

async def download(url):
    loop = asyncio.get_event_loop()
    log_file = url.split("/")[-1]
    # response = requests.get(url)
    response = await loop.run_in_executor(None, requests.get, url)
    with open(log_file,'w') as f:
        f.write(response.text)



async def main():
    start = time.perf_counter()
    url_logs=[]
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')
    for a in all_a:
        if a['href'].endswith('.log'):
            url_logs.append(f"{url}{a['href']}")
    
    tasks = []
    for url in url_logs:
        # tasks.append(download(url)) Old !
        tasks.append(download_aiohttp(url))

    await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f"{end-start:.2f}s")








if __name__=='__main__':
    asyncio.run(main())
