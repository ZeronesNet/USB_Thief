import os

def Get_FilesPath(CopyPath,Mix_GB):# ==> 返回一个包含所有文件的列表
    
    FilesList = os.listdir(CopyPath)
    # 根据配置的路径列出目录下的文件
    ALL_Files = []
    for file in FilesList:

        file = CopyPath + "\\" + file# 转换绝对路径
        filesize = os.path.getsize(file)

        if (os.path.isfile(file)) == True and filesize<= Mix_GB:# isfile内应为绝对路径
            ALL_Files.append(file)

    return(ALL_Files)

    # 通过处理后返回目标目录中的文件而不是文件夹
'''
def Get_DocPath(CopyPath):# ==> 返回一个包含所有文件夹的列表

    DocPath = os.listdir(CopyPath)
    # 根据配置的路径列出目录下的文件
    ALL_Doc = []
    for Doc in DocPath:

        Doc = CopyPath + "\\" + Doc# 转换绝对路径

        if (os.path.isdir(Doc)) == True:
            ALL_Doc.append(Doc)
    
    return(ALL_Doc)
    # 通过处理后返回目标目录中的文件夹而不是文件
'''
def Get_AllFiles(CopyPath,Mix_GB):# 返回一个列表包含目录以及子目录的文件

    AllFilesList = []
    for i in os.walk(CopyPath):

        ListLength = len(i)
        FatherPath = i[0]# 当前目录
        SonFile = i[ListLength - 1]# 目录下的文件

        for x in SonFile:

            file = FatherPath + "\\" + x # 文件的绝对路径
            if os.path.getsize(file) <= Mix_GB:
                AllFilesList.append(x)
        #AllFilesList = AllFilesList + i[ListLength - 1]
    return(AllFilesList)
if __name__ == "__main__":
    print("错误：模块不可直接运行")
#    Get_AllFiles(r"D:\Tools\IDM\IDM",1000)
#Running Normally
