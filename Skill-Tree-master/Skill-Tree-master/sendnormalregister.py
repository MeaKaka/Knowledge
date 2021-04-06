# -*- coding:utf-8 -*-
'''
CWQ:17.12.19,multi-srcIP
'''
# import json
# import operator
# from threading import Thread
#
# import dpkt
#
# from StrategyFunctions import *
# from imsSQL import markTaskEnd
# from app.tools import timenow
# from app.tools import constant
# import sys
#
# import os

import socket
import hashlib

# rawPKTPath = r"/usr/local/TYTXMN/SIPGEN"
sipIP = "192.168.51.147"
sipPort = 5060
fileLimit = 5
BUFSIZE = 1024 * 1024

# send mode
SINGLEPKT = 'SINGLEPKT'
FLOOD = 'FLOOD'
TYPE = 'TYPE'
STRATEGY = 'STRATEGY'

normalMsg = 'REGISTER sip:bj.ims.bupt.com SIP/2.0\r\n\
Via: SIP/2.0/UDP 192.168.50.101:6060;rport;branch=z9hG4bK5a5bf788-005495\r\n\
To: <sip:+8613612340002@bj.ims.bupt.com>\r\n\
From: <sip:+8613612340002@bj.ims.bupt.com>;tag=5a5bf5f5\r\n\
Contact: <sip:+8613612340002@192.168.50.101:6060;transport=udp>\r\n\
Call-ID: ZdmAg19053-ID00000001-H8M029S0@192.168.50.101\r\n\
CSeq: 1 REGISTER\r\n\
Max-Forwards: 70\r\n\
User-Agent: Chinamobile-Ucommunicator/vb3.2.1.88\r\n\
Expires: 300\r\n\
Allow: INVITE, MESSAGE, INFO, PRACK, PUBLISH,SUBSCRIBE, OPTIONS, UPDATE, BYE, CANCEL, NOTIFY, ACK, REFER\r\n\
Content-Length: 0\r\n\r\n'
# sampling
interval = 1
rate = 0.4
limit = 5

reg2BeforeNonce = 'REGISTER sip:bj.ims.bupt.com SIP/2.0\r\n\
Via: SIP/2.0/UDP 192.168.50.101:6060;rport;branch=z9hG4bK5a5bf81d-00068b\r\n\
To: <sip:+8613612340002@bj.ims.bupt.com>\r\n\
From: <sip:+8613612340002@bj.ims.bupt.com>;tag=5a5bf5f5\r\n\
Contact: <sip:+8613612340002@192.168.50.101:6060;transport=udp>\r\n\
Call-ID: ZdmAg19053-ID00000001-H8M029S0@192.168.50.101\r\n\
CSeq: 2 REGISTER\r\n\
Max-Forwards: 70\r\n\
User-Agent: Chinamobile-Ucommunicator/vb3.2.1.88\r\n\
Expires: 300\r\n\
Allow: INVITE, MESSAGE, INFO, PRACK, SUBSCRIBE, OPTIONS, UPDATE, BYE, CANCEL, NOTIFY, ACK, REFER\r\n\
Authorization: Digest username="+8613612340002@bj.ims.bupt.com",nonce="'
# nonce="b7c9036dbf3054a5a5bf75aea940e9703dc8f84c1508"
reg2AfterNonce = '",realm="bj.ims.bupt.com",uri="sip:bj.ims.bupt.com",qop=auth,nc=00000001,cnonce="715fdefb",opaque="",response="'
# response="7133c942ad62110f5ad794fccb63d31d"
reg2AfterResp = '",algorithm=MD5\r\n\
Content-Length: 0\r\n\r\n'
# data= 'SIP/2.0 401 Unauthorized\r\n\
# Call-ID: ZdmAg16217-ID00000001-H8M032S30@192.168.50.101\r\n\
# Via: SIP/2.0/UDP 192.168.50.101:6060;received=192.168.50.101;branch=z9hG4bK5a5c56af-007e56;rport=6080\r\n\
# To: <sip:+8613612340001@bj.ims.bupt.com>;tag=5a56c73e-5a5c56811d0fe45c\r\n\
# From: <sip:+8613612340001@bj.ims.bupt.com>;tag=5a5bf6c7\r\n\
# CSeq: 347 REGISTER\r\n\
# Date: Mon, 15 Jan 2018 07:21:37 GMT\r\n\
# Server: Alcatel-Lucent-HPSS/3.0.3\r\n\
# WWW-Authenticate: Digest realm="bj.ims.bupt.com",\r\n\
#    nonce="b7c9036dbf3054aea940e9703dc8f5a5c568184c2908",\r\n\
#    opaque="ALU:QbkRBthOEgEQAkgVEwwHRAIBHkNfQ18CGgcXERUZFVQjKG0mMDYzZiolJnZ4fnlg",\r\n\
#    algorithm=MD5,\r\n\
#    qop="auth"\r\n\
# Content-Length: 0\r\n\r\n'

sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendSocket.bind(("", 6060))


def main():
    # nonce="b7c9036dbf3054ae5a5c57a9a940e9703dc8f84c1608"
    username = "+8613612340002@bj.ims.bupt.com"
    realm = "bj.ims.bupt.com"
    password = "1111"
    # username="anonymous"
    # password=""
    cnonce = "715fdefb"
    requestMothod = "REGISTER"
    request_URI = "sip:bj.ims.bupt.com"

    global sipIP, sipPort, normalMsg
    while(1):
        sendSocket.sendto(normalMsg, (sipIP, sipPort))
        try:
            sendSocket.settimeout(3)
            data, ADDR = sendSocket.recvfrom(BUFSIZE)
            print ADDR
            state = data[0:12]
            print state
            print data
            # if "504" in state:
            #     return "ICSCF 宕机!"
            if "401" in state:
                #         读字段获取nonce的值
                nonceBeg = data.find('nonce', 0)
                nonceEnd = data.find('\r', nonceBeg)
                nonce = data[nonceBeg:nonceEnd]
                print "nonce:"
                print nonce
                nonce = nonce[7:-2]
                print nonce
                # m=hashlib.md5()
                # m.update(nonce)
                # response=m.hexdigest()
                # print "response:"
                # print response


                m = hashlib.md5()
                str1 = username + ":" + realm + ":" + password
                print str1
                m.update(str1)
                t1 = m.hexdigest()

                m22 = hashlib.md5()
                str22 = requestMothod + ":" + request_URI
                m22.update(str22)
                print str22
                t22 = m22.hexdigest()
                print t22

                m2 = hashlib.md5()
                # m2.update(requestMothod:request-URI)
                str2 = t1 + ":" + nonce + ":" + "00000001" + ":" + cnonce + ":" + "auth:" + t22
                print str2
                m2.update(str2)
                response = m2.hexdigest()
                # print response
                print response

                reg2Msg = reg2BeforeNonce + nonce + reg2AfterNonce + response + reg2AfterResp
                sendSocket.sendto(reg2Msg, (sipIP, sipPort))
                data, ADDR = sendSocket.recvfrom(BUFSIZE)
                print reg2Msg
        except Exception as e:
            print str(e)
            break


main()