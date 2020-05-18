import winreg
import time
import re

class_path="Software\Classes"
#everedit_time_path="Software\Classes\ZQBKAF8ATWBDADIAMWAZ"#注册表项，每台电脑可能不一样
#everedit_time_key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,everedit_time_path,0,winreg.KEY_ALL_ACCESS)
class_key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,class_path,0,winreg.KEY_ALL_ACCESS)
for i in range(winreg.QueryInfoKey(class_key)[0]):
    sub_path=winreg.EnumKey(class_key,i)
    if re.match('^[A-Z0-9]{20}$',sub_path):
        print("注册表项路径：",'\\'.join([class_path,sub_path]))
        everedit_time_key=winreg.OpenKey(class_key,sub_path,0,winreg.KEY_ALL_ACCESS)
        break
key_name,key_value,key_type=winreg.EnumValue(everedit_time_key,0)
old_time=int.from_bytes(key_value,'little')
print("上次试用注册时间：",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(old_time)))
new_time=int(time.time())
print("本次试用注册时间：",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(new_time)))
new_key_value=new_time.to_bytes(8,'little')
winreg.SetValueEx(everedit_time_key,'',0,key_type,new_key_value)
winreg.CloseKey(everedit_time_key)