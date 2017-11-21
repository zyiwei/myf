Flasky搭建的校园信息交互网站
=======
## 作品简介
你是不是经常为自己错过辅导员的年级通知而苦恼，你是不是想找导师但找不到他的具体信息，你是不是想给后勤人员反映意见但找不到渠道，...?我们认为这些都是校园信息交互不对称造成的，针对这个问题，我们开发了一个智慧校园信息交互网站，它具有如下特点：
1、辅导员、老师、学生、后勤人员都可以注册成为用户，大家可以相互关注。比如：我们可以很方便地在放假期间问食堂经理食堂开放时间。
2、老师可以发布教学信息，辅导员可以发布教务信息，并且网站还可以把重要的信息聚集在一起，避免学生漏看通知


## 功能介绍
#### 具体见功能介绍动图


## 环境搭建（MacOS)
#### 1.创建virtualenv
检查系统是否安装virtualenv:
$virtualenv --version

若结果报错：
$sudo easy_install virtualenv

#### 2.下载Github代码
$git clone https://github.com/miguelgrinberg/flasky.git

#### 3.在flasky文件夹中创建虚拟环境
进入下载的文件目录:
$cd flasky

将创建的虚拟环境命名为venv:
$virtualenv venv

激活虚拟环境:
$source venv/bin/activate

#### 4.配置虚拟环境
安装依赖：
(venv)$pip install -r requirements/dev.txt

(配置邮箱用户、管理员自动识别邮箱及服务器，若想直接试用网站默认账户，可跳过此步骤）：
(venv)$export MAIL_USERNAME=<你的邮箱>

(venv)$export MAIL_PASSWORD=<邮箱服务器密码>

(venv)$export FLASKY_ADMIN=<管理员邮箱>

(venv)$export MAIL_SENDER=<服务器发送邮件邮箱>

#### 5.网站初始账户
#####（1)管理员账户：
    邮箱：admin@example.com 密码：admin
##### (2)协管员账户(6个)：
    邮箱：mod1@example.com 密码：mod1
    邮箱：mod2@example.com 密码：mod2
    ......
    邮箱：mod3@example.com 密码：mod6

#### 6.运行程序
(venv)$python manage.py