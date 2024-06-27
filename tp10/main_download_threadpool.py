import threading
import requests
from bs4 import BeautifulSoup
import time
import argparse
import concurrent.futures
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

def download(url):
    log_file = url.split("/")[-1]
    response = requests.get(url)
    with open(log_file,'w') as f:
        f.write(response.text)


def main(url):
    logger.warning(url)
    start = time.perf_counter()
    url_logs=[]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')
    for a in all_a:
        if a['href'].endswith('.log'):
            url_logs.append(f"{url}{a['href']}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:    
        executor.map(download,url_logs)

    end = time.perf_counter()
    print(f'{end-start:.2f}s')

if __name__=='__main__':
    a = argparse.ArgumentParser()
    a.add_argument('--url',help="url to parse",default="https://logs.eolem.com/")
    params = a.parse_args()
    main(params.url)
