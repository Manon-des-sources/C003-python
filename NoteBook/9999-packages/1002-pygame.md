# 一、安装pygame
* 到[pygame官网](http://www.pygame.org/download.shtml)下载：  
![photo](0000-photos/0035.png)  
* 安装过程中会要求选择python 版本：  
![photo](0000-photos/0034.png)  
比如上面绿色框内的pygame版本要求python2.7，而红色框内的pygame版本要求python3.2  
如果版本不对、这一步就不能检测到python，安装后就无法使用  
红色框内的pygame版本要求python3.2、就必须是python3.2，python3.4都不行  
* 提示：  
另外、pygame要求安装新版时必须卸载旧版，而卸载旧版就必须运行旧版的安装程序、选择卸载  
新版安装程序是没有卸载旧版的功能的、只能卸载自己这个版本  
* 安装成功后、import pygame就知道能不能使用了：  
![photo](0000-photos/0036.png)  
也可以打卡一个游戏示例(路径：C:\Python27\Lib\site-packages\pygame\examples)：  
![photo](0000-photos/0040.png)  

# 二、运行程序
* python shell  
在python shell 运行pygame 代码可能会出现游戏窗口卡死的情况  
这是由于python shell 和pygame 有冲突  
![photo](0000-photos/0041.png)  

* cmd  
在cmd 里面调用pygame 代码，就不会有这个问题  
![photo](0000-photos/0043.png)  
![photo](0000-photos/0042.png)  

* 更多内容见官网或help  
![photo](0000-photos/0001.png)  
