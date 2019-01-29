import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/200/300')# str or request object
cat_img = response.read()
# req = urllib.request.Request('http://placekitten.com/g/500/600')
# response = urllib.request.urlopen(req)
response.geturl()
a = response.info()
print(a)#含有header
response.getcode()#http的状态
urlopen(url, data=None) #默认data是none就是用get如果赋值就用post提交

with open('cat.jpg' , 'wb') as f: #write bits
    f.write(cat_img)
