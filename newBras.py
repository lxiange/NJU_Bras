#Login Bras
from urllib import request, parse
def login(userid,passwd,mode='login'):
    if (mode=='login'):    #   1 is login
        requestURL='http://p.nju.edu.cn/portal_io/login'
        postData={'username':userid,'password':passwd}
        dataEncode=parse.urlencode(postData)
        req = request.Request(url = requestURL,data = dataEncode.encode('utf-8'))
    elif(mode=='logout'):   #   0 is logout
        requestURL='http://p.nju.edu.cn/portal_io/logout'
        req = request.Request(url = requestURL)
    else:
        print ('Fuck you!')

    res_data = request.urlopen(req)
    res = res_data.read()
    print (res.decode('utf-8'))
    print (res)

login('1312200xx','password')    #   fill it!

