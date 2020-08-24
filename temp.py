import random
import json
import requests


# Create your views here.
def lotto(request):
    r = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=836')
    response = r.json()
    bonus = response.get('bnusNo')
    numbers = []
    for i in response:
        print(i)

    context = {
        'numbers': numbers,
        'bonus': bonus,
    }

