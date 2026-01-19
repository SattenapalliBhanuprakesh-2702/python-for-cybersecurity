import requests

api="https://api.github.com/repos/python/cpython"
data=requests.get(api).json()
for key,value in data.items():
    print("{",key,":",value,"}")
    print("\n")
# print("stars:",data["stargazers_count"])
# print("Language:",data["Language"])