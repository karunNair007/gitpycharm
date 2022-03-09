import json


import requests

url='https://jsonplaceholder.typicode.com/posts'

fileread=open('E:\KRN Files\Python\API Testing\POST\Post.txt','r').read()
print(fileread)

jn=json.loads(fileread)
print(jn)

respond=requests.post(url,fileread)
print(respond)



