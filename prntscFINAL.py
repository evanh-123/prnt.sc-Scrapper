import requests
from requests_html import HTMLSession
import random
import string
from mega import Mega
mega = Mega()
import os
import shutil

email = 'evanhodges2078@gmail.com'
password = 'Qedz250E!'
m = mega.login(email, password)

def hello():
    hello.counter += 1
    print(hello.counter)
hello.counter = 0

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    global s
    s = (''.join(random.choice(chars) for _ in range(size)))

image_urls = set()
def get_images():
    id_generator()
    global url
    url = (f"https://prnt.sc/{s}")
    try:
        session = HTMLSession()
        response = session.get(url)
     
    except requests.exceptions.RequestException as e:
        print(e)
    images = response.html.xpath('//*[@id="screenshot-image"]')
    for image in images:
        global src
        src = image.attrs["src"]

get_images()
while src == 'st.prntscr.com/2022/02/22/0717/img/0_173a7b_211be8ff.png':
    get_images()
    print('Deleted Image :(')
else:
    pass

fnurl = f'{src}'
print('Found Image! Uploading to Mega...')
def uploadimgtomega():
    hello()
    filename = f"Image{hello.counter}.jpeg"
    r = requests.get(fnurl, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
        f.close()

    folder_Id = m.find_path_descriptor('test')
    m.upload(filename, folder_Id)
    os.remove(filename)

while True:
    get_images()
    while src == 'st.prntscr.com/2022/02/22/0717/img/0_173a7b_211be8ff.png':
        get_images()
        print('Deleted Image :(')
    else:
        pass
    fnurl = f'{src}'
    with open('urls.txt', 'a') as f:
        f.write(f'{fnurl}\n')
        f.close()
    print('Found Image! Uploading to Mega...')
    uploadimgtomega()
