import winreg
import time

everedit_time_path="Software\Classes\ZQBKAF8ATWBDADIAMWAZ"#注册表项，每台电脑可能不一样
everedit_time_key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,everedit_time_path,0,winreg.KEY_ALL_ACCESS)
key_name,key_value,key_type=winreg.EnumValue(everedit_time_key,0)
old_time=int.from_bytes(key_value,'little')
print("上次试用注册时间：",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(old_time)))
new_time=int(time.time())
print("本次试用注册时间：",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(new_time)))
new_key_value=new_time.to_bytes(8,'little')
winreg.SetValueEx(everedit_time_key,'',0,key_type,new_key_value)
winreg.CloseKey(everedit_time_key)