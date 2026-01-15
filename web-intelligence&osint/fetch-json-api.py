import requests

api="https://api.github.com/repos/python/cpython"
data=requests.get(api).json()
print(data)
# print("stars:",data["stargazers_count"])
# print("Language:",data["Language"])