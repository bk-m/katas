"""
Kassel: 12596885
Stadtkreis Kassel: 665077
Göttingen: 657171
# Hann. Münden: 2867613
"""

import requests
import json

def get_weather():
    ks = requests.get('https://api.dronestre.am/data')
    return ks.json()

def main():
    tmp = get_weather()
    print(tmp)

if __name__ == '__main__':
    main()
