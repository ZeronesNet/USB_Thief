# 此模块用于检查配置文件是否存在，不存在则生成一个
# Settings.append(ini_read.replace("\n",""))# replace 方法替换转义字符为空字符串
import os 

def CheckPath():
    LocalPath = os.getcwd()
    checkpath = LocalPath + r"\USBthief.ini"

    if os.path.exists(checkpath) == True:

        OpenPath = LocalPath + r"\USBthief.ini"
        USBthief = open(OpenPath,"rb")
        Setting = USBthief.readlines()

        CopyPath = Setting[6].decode("UTF-8").replace("\n","")
        Mix_GB = Setting[9].decode("UTF-8").replace("\n","")
        Copy_Choice = Setting[12].decode("UTF-8").replace("\n","")
        TargetEnd = Setting[15].decode("UTF-8").replace("\n","")
        TargetEnd = TargetEnd.split()   

        Setting = []
        Setting.append(CopyPath.replace("\r",""))
        Setting.append(Mix_GB.replace("\r",""))
        Setting.append(Copy_Choice.replace("\r",""))
        return(Setting,TargetEnd)
        # 配置文件读取并处理
     
    elif os.path.exists(checkpath) == False:

        os.system("echo.>>" + checkpath)
        Writeini = open(checkpath,"w")

        Writeini.write("# print(\"1 ==> 提取目录下所有文件\")\n")
        Writeini.write("# print(\"2 ==> 键入格式名以提取特定格式的文件\")\n")
        Writeini.write("# print(\"3 ==> 提取目标目录以及子目录的特定文件\")\n")
        Writeini.write("# print(\"后续可通过修改ini文件以改变初始配置\")\n\n")


        Writeini.write("[读取位置][5]\n")
        Writeini.write("D:\\\n\n")
        # 读取位置
        Writeini.write("[单个文件大小][8]\n")
        Writeini.write("2\n\n")
        # 单个文件大小
        Writeini.write("[读取操作][11]\n")
        Writeini.write("1\n\n")
        # 读取操作
        Writeini.write("[文件后缀][14]\n")
        Writeini.write("txt")
        # 文件后缀

        Writeini.close()

if __name__ == '__main__':
    print("此模块不可直接运行")