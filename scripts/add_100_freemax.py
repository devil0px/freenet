
import hashlib
import requests, time


# -----------------------------------


def add_100mg(number,number2,password):
    url2= "https://services.orange.eg/GetToken.svc/GenerateToken"
    headers2={
        "Content-Type": "application/json; charset\u003dUTF-8",
        "Content-Length": "78",
        "Host": "services.orange.eg",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9"
      }
    data2='{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
    re2=requests.post(url2,headers=headers2,data=data2).json()
    ctv1=re2["GenerateTokenResult"]
    ctv=ctv1["Token"]
    h = hashlib.sha256((ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest()
    htv=h.upper()
    urrrlll="https://services.orange.eg/SignIn.svc/SignInUser"
    hd={
    "_ctv":ctv,
    "_htv":htv,
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"168",
    "Host":"services.orange.eg",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/3.14.9"
    }

    data2='{"appVersion": "6.0.1","channel":{"ChannelName":"MobinilAndMe", "Password": "ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"'+number+'","isAndroid": "true","password":"'+password+'"}'

    r=requests.post(urrrlll, headers=hd, data=data2)
    userid=r.json()["SignInUserResult"]["UserData"]["UserID"]
    url = "https://backend.orange.eg/api/HybridFamily/ManageSharing"
    headers = {
    "_ctv":ctv,
    "_htv":htv,
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "256",
    "Host": "services.orange.eg",
    "Connection": "Keep-Alive",
    "User-Agent": "okhttp/3.14.9"
    }       
    json ={"ActionType":"2","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"FamilyMemberDial":number2,"lang":"en","Sharing":[{"SharedAmount":"1","SharingType":5}],"dial":number,"IsEasyLogin":'false',"password":password}

    
    rec=requests.post(url, headers=headers, json=json).json()['ErrorDescription']
    print (rec)
   
    if rec == "انت استخدمت البرومو كود النهاردة":
        return False , rec
    else:
        return rec
    
    


if __name__ == "__main__":

  print(add_100mg('01285238180','abdo'))

