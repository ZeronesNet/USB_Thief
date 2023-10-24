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
        for e in File_end:
            for e1 in TargetEnd:
                if e == e1:
                    Files_Check.append(SingleFile)
        # 取得单个后缀，与TargetEnd中的后缀进行对比
    return(Files_Check)

if __name__ == '__main__':
    print("此模块不可直接运行")
