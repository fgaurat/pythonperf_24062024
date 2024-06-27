from bs4 import BeautifulSoup
import time
import requests
import asyncio
import aiohttp

async def download(queue_url,queue_save):
    while True:
        url = await queue_url.get()
        log_file = url.split("/")[-1]
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                print("download",log_file)
                data = {
                    "log_file":log_file,
                    "text":text
                }
                queue_save.put_nowait(data)

        queue_url.task_done()

async def save(queue):
    while True:
        data = await queue.get()
        log_file = data['log_file']
        text = data['text']
        print("write",log_file)
        with open(log_file,'w') as f:
            f.write(text)

        queue.task_done()


async def main():
    start = time.perf_counter()

    queue_url = asyncio.Queue()
    queue_save = asyncio.Queue()

    nb_download_workers = 10
    nb_save_workers = 10

    url_logs=[]
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')
    for a in all_a:
        if a['href'].endswith('.log'):
            url_logs.append(f"{url}{a['href']}")
    
    tasks = []
    for i in range(nb_download_workers):
        task=asyncio.create_task(download(queue_url,queue_save))
        tasks.append(task)

    for i in range(nb_save_workers):
        task = asyncio.create_task(save(queue_save))
        tasks.append(task)
    
    for url in url_logs:
        queue_url.put_nowait(url)

    await queue_url.join()
    await queue_save.join()
    [task.cancel() for task in tasks]

    end = time.perf_counter()
    print(f"{end-start:.2f}s")

    

if __name__=='__main__':
    asyncio.run(main())
    
