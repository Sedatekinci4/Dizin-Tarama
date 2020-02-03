import requests

file = open("common.txt","r")
url = 'http://alperenkayademir.com/'
for x in file:
    r =requests.get(url+x)
    print(url+x)
    print(r.status_code)
    if(r.status_code == 200):
        print("Dizin var!!!!!!!")
    else:
        print("---")