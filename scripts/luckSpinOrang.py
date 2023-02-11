import hashlib
import json

import requests


def Htv_Ctv():
    url2 = "https://services.orange.eg/GetToken.svc/GenerateToken"
    headers2 = {
        "Content-Type": "application/json; charset\u003dUTF-8",
        "Content-Length": "78",
        "Host": "services.orange.eg",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9"
    }
    data2 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
    re2 = requests.post(url2, headers=headers2, data=data2).json()
    ctv1 = re2["GenerateTokenResult"]
    ctv = ctv1["Token"]
    h = hashlib.sha256((ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest()
    htv = h.upper()
    return ctv, htv


def luck_spin(number, password):
    ctv, htv = Htv_Ctv()
    hd = {
        "_ctv": ctv,
        "_htv": htv,
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "168",
        "Host": "services.orange.eg",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9"
    }

    data = {"ChannelName": "MobinilAndMe", "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF", "Dial": number,
            "Language": "ar", "Password": password, "ServiceClassId": "1065"}

    spin = requests.post('https://services.orange.eg/APIs/Gaming/api/WheelOfFortune/Spin', headers=hd,
                         data=json.dumps(data)).json()
    try:
        OfferId = spin['OfferDetails']['OfferId']
        CategoryId = spin['SecondryButtonDetails']['CategoryId']

        ctv, htv = Htv_Ctv()
        readem_data = {"CategoryId": CategoryId, "ChannelName": "MobinilAndMe",
                       "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF",
                       "Dial": number, "Language": "ar", "OfferId": OfferId, "Password": password,
                       "ServiceClassId": "1065"}
        readem_hd = {
            "IsAndroid": "true",
            "OsVersion": "9",
            "AppVersion": "6.8.0",
            "_ctv": ctv,
            "_htv": htv,
            "isEasyLogin": "false",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "191",
            "Host": "services.orange.eg",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.14.9",
        }

        readem = requests.post('https://services.orange.eg/APIs/Gaming/api/WheelOfFortune/Fulfill', headers=readem_hd,
                               data=json.dumps(readem_data)).json()
        return readem

    except:
        return False , spin['ErrorDescription']


if __name__ == '__main__':
    luck_spin('01220232580', 'anas01060A@')
