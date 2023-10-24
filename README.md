# USB_Thief v0.6
## 可以将脚本部署在u盘中实现复制主机文件的功能，在Windows系统中通过测试。
### USB Thief.py为主文件，其余两个.py文件为支持库
### 库文件说明：
#### Get_FilesAndDoc.py用于获取目标路径的所有文件
#### Check_ini.py用于检查或创建配置文件
#### Check_file.py用于检查多后缀和后缀混淆的问题
### 计划 v1.0 发布第一个可用的包更新

 2023/10/5 实现预期功能 下一步将实现遍历子文件夹进行复制的功能
 
 2023/10/6 解决了只能复制单个文件的错误 实现了提取目标目录以及子目录的所有特定格式的文件
 
 2023/10/7 实现主要的三个函数的模块化 缩减了主文件的代码量

 2023/10/7 v0.2 解决了只能识别三个的后缀名的bug 现在可以识别所有文件后缀名称了 但仍在试图解决双后缀的问题

 2023/10/12 军训以及sbDY的原因，今天才更新。v0.3 加入自动识别配置文件的功能以及添加了识别文件大小的功能（暂时支持选项1）

 2023/10/12 识别文件大小的功能支持全部选项！！！

 2023/10/13 将主文件的部分代码移植到模块中，取消了input交互方式(原代码仍然存在)，更改为ini配置文件的方式，提升了脚本运作时的隐匿性

 2023/10/18 v0.4 删除了模块中的input语句，现在脚本运行会将ini设置默认模式。下一版本将会解决运行命令产生的cmd黑框
 
 2023/10/20 v0.5更改主文件的运行逻辑，防止copy命令执行错误时卡死脚本

 2023/10/24 v0.6创建
