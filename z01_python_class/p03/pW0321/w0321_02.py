import requests
res = requests.get("http://www.google.com/")
res.raise_for_status()  #   에러코드이면 자동멈춤

print("총 문자길이: ",len(res.text))

with open("google.html","w",encoding="utf8") as f:
    f.write(res.text)