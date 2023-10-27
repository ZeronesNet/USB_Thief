# CheckPath方法用于检查配置文件是否存在，不存在则生成一个
# Settings.append(ini_read.replace("\n",""))# replace 方法替换转义字符为空字符串
import os 

def CheckPath():
    LocalPath = os.getcwd()
    checkpath = LocalPath + r"\USBthief.ini"

    if os.path.exists(checkpath) == True:

        OpenPath = LocalPath + r"\USBthief.ini"
        USBthief = open(OpenPath,"rb")
        Setting = USBthief.readlines()

        CopyPath = Setting[8].decode("UTF-8").replace("\n","")
        Mix_GB = Setting[11].decode("UTF-8").replace("\n","")
        Copy_Choice = Setting[14].decode("UTF-8").replace("\n","")
        TargetEnd = Setting[17].decode("UTF-8").replace("\n","")
        TarFile_Name = Setting[20].decode("UTF-8").replace("\n","")
        TargetEnd = TargetEnd.split()
        TarFile_Name = TarFile_Name.split()

        Setting = []
        Setting.append(CopyPath.replace("\r",""))
        Setting.append(Mix_GB.replace("\r",""))
        Setting.append(Copy_Choice.replace("\r",""))
        return(Setting,TargetEnd,TarFile_Name)
        # 配置文件读取并处理
     
    elif os.path.exists(checkpath) == False:

        os.system("echo.>>" + checkpath)
        Writeini = open(checkpath,"w")

        Writeini.write("# 1 ==> 目标文件夹的所有文件提取\n")
        Writeini.write("# 2 ==> 目标文件夹的特定文件提取\n")
        Writeini.write("# 3 ==> 目标文件夹及其子文件夹的所有文件提取\n")
        Writeini.write("# 4 ==> 目标文件夹及其子文件夹的特定文件提取\n")
        Writeini.write("# 后续可通过修改ini文件以改变初始配置\n\n")


        Writeini.write("[读取位置][8]\n")
        Writeini.write("D:\\\n\n")
        # 读取位置
        Writeini.write("[单个文件大小][11]\n")
        Writeini.write("2\n\n")
        # 单个文件大小
        Writeini.write("[读取操作][14]\n")
        Writeini.write("1\n\n")
        # 读取操作
        Writeini.write("[文件后缀][17]\n")
        Writeini.write("txt\n\n")
        # 文件后缀
        Writeini.write("[目标文件名][21]\n")
        Writeini.write("测试")
        # 目标文件名

        Writeini.close()
if __name__ == '__main__':
    print("此模块不可直接运行")