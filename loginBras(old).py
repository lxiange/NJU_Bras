#Login Bras
#Due to the update of 'http://p.nju.edu.cn',
#this code no more works,
#just for back up.

import urllib2
import urllib
def login(userid,passwd,mode):
    requestURL='http://p.nju.edu.cn/portal/portal_io.do'
    if (mode==1):    #   1 is login
        postData={'action':'login','username':userid,'password':passwd}
    elif(mode==0):   #   0 is logout
        postData={'action':'logout'}
    else:
        print 'Fuck you!'
    dataEncode=urllib.urlencode(postData)
    req = urllib2.Request(url = requestURL,data = dataEncode)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


login('1312200xx','password',0)    #   fill it!
