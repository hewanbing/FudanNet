# FudanNet
1. 文件说明:
   1.1 fudanNet.py
       校园网登录验证
   1.2 aha.py
       疫情打卡

2. 软件环境依赖
   不同操作系统安装方法不一样,以下为Ubuntu系统安装方法

   2.1 安装python3
       sudo apt install python3
   2.2 安装python包管理器pip
       sudo apt install python3-pip
   2.3 安装python模块selenium
       pip3 install selenium
   2.4 安装firefox及驱动
       确保已安装firefox浏览器
       拷贝geckodriver到/usr/bin/
       sudo cp gechodriver /usr/bin/

3. 使用方法

   3.1 打开crontab编辑器
       crontab -e
   3.2 在编辑器最后添加如下内容(如果不需要复旦网络验证可以省略第一条)
       10  3  *  *  *  python3  (脚本存放路径)/fudanNet.py  你的复旦工号  密码
       0   8  *  *  *  python3  (脚本存放路径)/aha.py       你的复旦工号  密码
       (可根据实际需要修改以上数字，第一个是分钟，第二个是小时，后面星号不要变)
   3.3 编辑器保存退出并查看定时任务
       crontab -l
   