import requests

from celery import task


@task()
def urlopen(url):
    print('Opening: {0}'.format(url))
    try:
        response = requests.get(url)
    except Exception as exc:
        print('URL {0} gave error: {1!r}'.format(url, exc))
    return len(response.text)
