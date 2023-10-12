# 此模块用于检查配置文件是否存在，不存在则生成一个

import os 

def CheckPath():
    localpath = os.getcwd()
    checkpath = localpath + r"\USBthief.ini"

    if os.path.exists(checkpath) == True:
        print("true")
    elif os.path.exists(checkpath) == False:
        os.mkdir(checkpath)
        Writeini = open(checkpath,"w")

        CopyPath = input("请输入文件的保存地址：")
        Mix_GB = input("请输入单次文件传输的最大值(GB)：")
        Writeini.write(CopyPath)
        Writeini.write(Mix_GB)
        Writeini.write("END")

        Writeini.close()

if __name__ == '__main__':
    print("此模块不可直接运行")