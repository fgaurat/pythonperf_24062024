from celery import Celery,signature,group,chain
from bs4 import BeautifulSoup
import requests

# celery -A celery_tasks worker --loglevel=INFO -P solo
def main():
    app = Celery('tasks', broker='pyamqp://guest@localhost//',backend="rpc://")
    
    # result = app.send_task('celery_tasks.add',args=[2,2])
    # print(result.get())
    # result = app.send_task('celery_tasks.download',args=["http://logs.eolem.com/apache_logs_01.log"])
    # print(result.get())

    download = signature("celery_tasks.download")
    # result =download.delay("http://logs.eolem.com/apache_logs_01.log")
    # print(result.get())

    url_logs=[]    
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')
    for a in all_a:
        if a['href'].endswith('.log'):
            url_logs.append(f"{url}{a['href']}")

    # # download
    # download_tasks = [signature("celery_tasks.download",args=[url]) for url in url_logs]
    # download_group = group(download_tasks)
    # result = download_group()
    # # print(result.get())
    # # save
    # save_tasks = [signature("celery_tasks.save",args=[to_save]) for to_save in result.get()]
    # save_group = group(save_tasks)
    # result = save_group()


    for url in url_logs:
        chain(
            signature("celery_tasks.download",args=[url]),
            signature("celery_tasks.save")       
        )()


if __name__=='__main__':
    main()
