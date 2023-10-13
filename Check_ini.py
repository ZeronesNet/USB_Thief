# 此模块用于检查配置文件是否存在，不存在则生成一个

import os 

def CheckPath():
    localpath = os.getcwd()
    checkpath = localpath + r"\USBthief.ini"

    if os.path.exists(checkpath) == True:
        print("true")
    elif os.path.exists(checkpath) == False:

        print("1 ==> 提取目录下所有文件")
        print("2 ==> 键入格式名以提取特定格式的文件")
        print("3 ==> 提取目标目录以及子目录的特定文件")
        print("后续可通过修改ini文件以改变初始配置")

        os.system("echo.>>" + checkpath)
        Writeini = open(checkpath,"w")

        CopyPath = input("请输入文件的保存地址：")
        Mix_GB = input("请输入单次文件传输的最大值(GB)：")
        CopyChoice = input("请输入初始选择：")
        TargetEnd = input("请输入特定的文件后缀：")
        Writeini.write(CopyPath)
        Writeini.write(Mix_GB)
        Writeini.write(CopyChoice)
        Writeini.write(TargetEnd)
        Writeini.write("END")

        Writeini.close()

if __name__ == '__main__':
    print("此模块不可直接运行")