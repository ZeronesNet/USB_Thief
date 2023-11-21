def Check_file(FilesList,TargetEnd):
    # 传入一个文件路径的列表
    Files_Check = []
    
    for SingleFile in FilesList:

        File_end = []
        SingleFile_Listed = list(SingleFile)
        # 对每个元素进行列表化处理
        DelMark = []
        num = 1
        for a in range(1,len(SingleFile_Listed)):
            if SingleFile_Listed[num] == SingleFile_Listed[num -1] and SingleFile_Listed[num] == '.':
                DelMark.append(num - 1)
            num = num + 1
        # 处理得到列表中所有'.'的序数并用DelMark接收
        num = 0
        for b in DelMark:
            Del = b - num
            SingleFile_Listed.pop(Del)
            num = num + 1
        # 处理列表得到一个去后缀混淆的列表
        PointMark = []
        num = 0
        for c in SingleFile_Listed:
            if c == '.':
                PointMark.append(num)
            num = num + 1
        PointMark.append(len(SingleFile_Listed))
        # 标记列表中的'.'元素
        num = 0
        for d in range(1,len(PointMark)):
            Filend = SingleFile_Listed[PointMark[num] + 1:PointMark[num + 1]]
            num = num + 1
            String = ''
            for d1 in Filend:
                String = String + d1
            File_end.append(String)
        # 提取所有可能的后缀
        # 提取后缀的列表# ====》["py","exe"]
        for e in File_end:
            for e1 in TargetEnd:
                if e == e1:
                    Files_Check.append(SingleFile)
        # 取得单个后缀，与TargetEnd中的后缀进行对比
    return(Files_Check)
def NameCheck(FileList,TarFile_Name):
    
    AfterCheck_list = []

    for SingleFile in FileList:

        Possible_Name = []
        SingleFile_list = list(SingleFile)
        PointLocation = SingleFile_list.index(".")
        FileName = SingleFile_list[0:PointLocation]
        # 取得文件的文件名列表
        num0 = 0
        num1 = 1
        num2 = 0
        num3 = 2
        FOR_Num = (len(FileName) * (len(FileName) - 1)) / 2
        FOR_Num = int(FOR_Num)

        while num0 < FOR_Num:
            for a in range(0,len(FileName) - num1):
                name = ""
                for b in FileName[num2:num3]:
                    name = name + b
                Possible_Name.append(name)
                num2 = num2 + 1
                num3 = num3 + 1
            num2 = 0
            num0 = num0 + len(FileName) - num1
            num1 = num1 + 1
            num3 = num1 + 1
        # 根据名称长度实现for循环顺序减1次运行
        # 求出文件名可能的组合并用Possible_Name接收
        for x in TarFile_Name:
            for y in Possible_Name:
                if x == y:
                    AfterCheck_list.append(SingleFile)

    # 方案一适用于精确搜索以及部分情况下的模糊搜索

    for SingleFile1 in FileList:
        
        PossibleNum = 0
        SingleFile1_list = list(SingleFile1)
        PointLocation1 = SingleFile1_list.index(".")
        FileName1 = SingleFile1_list[0:PointLocation1]
        # 列表化文件名称
        for x in TarFile_Name:
            x = list(x)
            for y in x:
                for z in FileName1:
                    if y == z:
                        PossibleNum = PossibleNum + 1
        # 通过三个for循环判断输入名称与文件名称的相同性
        if PossibleNum >= 2:
            AfterCheck_list.append(SingleFile1)
    # 方案二适用于模糊搜索    
    # ['你好啊.exe', 'hello.exe', '你好啊.exe', 'hello.exe']
    try:
        for i in AfterCheck_list:
            num = AfterCheck_list.index(i)
            for i1 in AfterCheck_list[num + 1:len(AfterCheck_list)]:
                if i == i1:
                    AfterCheck_list.pop(num + 1)
                num = num +1
        return(AfterCheck_list)
    except:
        return(AfterCheck_list)
    # 处理列表中的相同元素
    # 注意，当列表中相同元素超过两个时，程序出错



if __name__ == '__main__':
    print("此模块不可直接运行")