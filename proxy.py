import winreg
import ctypes
import time

#设置地址,没有使用过代理可能会不存在键报错
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0, winreg.KEY_ALL_ACCESS)
#设置刷新
INTERNET_OPTION_REFRESH = 37
INTERNET_OPTION_SETTINGS_CHANGED = 39
internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

#修改键值
def set_key(name, value):
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

#启用代理
def proxy_run(ip,port):
    set_key('ProxyEnable', 1) #启用
    #set_key('ProxyOverride', u'*.local;<local>') # 绕过本地代理设置
    set_key('ProxyServer', f'{ip}:{port}') #代理IP及端口，将此代理修改为自己的代理IP
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0,INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)

#停用代理
def proxy_stop():
    set_key('ProxyEnable', 0) #停用
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0,INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)