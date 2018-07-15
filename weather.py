import urllib.request
import json
import re

def main():
    name = '93452'
    key = '4d9cffc8109f4e2f9be310685d5ab9c6'
    url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + name + ',us&appid=' + key
    print(url)
    html = urllib.request.urlopen(url)
    print(html)
    data = json.loads(html.read())
    print(data)
    list1 = data['main']
    print(list1['temp'])


if __name__ == '__main__':
    main()
