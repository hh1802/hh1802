# URL - Uniform Resource Locator

import requests
import json


def main():
    # request / response
    resp = requests.get('http://api.tianapi.com/meinv/?key=a78efafa3bb9d348860c2f7c962adc78&num=10')
    mydict = json.loads(resp.text)
    for tempdict in mydict['newslist']:
        pic_url = tempdict['picUrl']
        resp = requests.get(pic_url)
        filename = pic_url[pic_url.rfind('/') + 1:]
        try:
            with open(filename, 'wb') as fs:
                fs.write(resp.content)
        except IOError as e:
            print(e)


if __name__ == '__main__':
    main()
