#!/usr/bin/env python3

"""
v1.0

useage:
    >>> python3 bras.py i yourid yourpassword    //login
    >>> python3 bras.py o                        //logout

    You should modify the var "interFace", 
    set the proper IP of the interface you want to login you bras.

    Next version will support AUTO select interface.
    
"""
import http.client, json, sys
from urllib import request, parse

def LogInOut(userid='',passwd='',mode='login',source_IP_PORT=None):
    """LogIn/Out Bras via specified interface"""
    assert mode in ['login','logout']

    serverAddr = 'p.nju.edu.cn'
    postAddr = '/portal_io/'+ mode
    postDict = {'username':userid,'password':passwd}
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"} #necessary!

    dataEncoded = parse.urlencode(postDict)
    conn = http.client.HTTPConnection(serverAddr,source_address=source_IP_PORT)
    conn.request("POST", postAddr, body=dataEncoded ,headers=headers )
    repStr = conn.getresponse().read().decode('utf-8')
    print(repStr)
    #repCode = json.loads(repStr)['reply_code']
    #print(repCode)
    
'''
#choose the target interface and choose a random port
#like:
interFace=('172.26.23.141',54236)
interFace=('114.212.122.123',26345)
'''
#interFace1=('172.26.116.52',23432)
interFace2=('192.168.1.108',24252)
###############

'''
if sys.argv[1]=='i':
    assert len(sys.argv)==4
    LogInOut(sys.argv[2],sys.argv[3], source_IP_PORT=interFace)
elif sys.argv[1]=='o':
    LogInOut(mode='logout')
'''
#LogInOut('9711002','9711002', source_IP_PORT=interFace1)
LogInOut('131220088','123456', source_IP_PORT=interFace2)
'''
LogInOut(mode='logout',source_IP_PORT=interFace1)
LogInOut(mode='logout',source_IP_PORT=interFace2)
'''
