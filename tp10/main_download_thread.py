import threading
import requests
from bs4 import BeautifulSoup
import time


def download(url):
    log_file = url.split("/")[-1]
    response = requests.get(url)
    with open(log_file,'w') as f:
        f.write(response.text)


def main():
    start = time.perf_counter()
    url_logs=[]
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')
    for a in all_a:
        if a['href'].endswith('.log'):
            url_logs.append(f"{url}{a['href']}")

    all_threads= []
    for url in url_logs:
        th = threading.Thread(target=download,args=[url])
        all_threads.append(th)
        th.start()
    
    [th.join() for th in all_threads]
    

    end = time.perf_counter()
    print(f'{end-start:.2f}s')

if __name__=='__main__':
    main()
