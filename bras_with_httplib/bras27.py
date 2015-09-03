#!/usr/bin/env python2

import httplib, json, sys, random
import urllib

def LogInOut(userid='',passwd='',mode='login',source_IP_PORT=None):
    """LogIn/Out Bras via specified interface"""
    assert mode in ['login','logout']

    serverAddr = 'p.nju.edu.cn'
    postAddr = '/portal_io/'+ mode
    postDict = {'username':userid,'password':passwd}
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"} #necessary!

    dataEncoded = urllib.urlencode(postDict)
    conn = httplib.HTTPConnection(serverAddr,source_address=source_IP_PORT)
    conn.request("POST", postAddr, body=dataEncoded ,headers=headers )
    repStr = conn.getresponse().read()
    print repStr
    #repCode = json.loads(repStr)['reply_code']
    #print(repCode)
    

interFace1=('10.0.2.15',random.randint(2048, 65533))
#interFace2=('172.26.127.174',random.randint(2048, 65533))


LogInOut('131220088','123456', source_IP_PORT=interFace1)
#LogInOut('','', source_IP_PORT=interFace2)

