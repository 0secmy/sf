# sf
爆破敏感文件  
.git泄露
测试

    http://www.example.com/.git/config

利用工具

GitHack、gittools（推荐）、dvcs-ripper
.SVN泄露
测试

    http://www.exmaple.com//.svn/entries

利用工具

dvcs-ripper
网站备份压缩文件
WEB-INF/web.xml泄露

WEB-INF主要包含一下文件或目录：

    /WEB-INF/web.xml：Web应用程序配置文件，描述了 servlet 和其他的应用组件配置及命名规则。
    /WEB-INF/classes/：含了站点所有用的 class 文件，包括 servlet class 和非servlet class，他们不能包含在 .jar文件中
    /WEB-INF/lib/：存放web应用需要的各种JAR文件，放置仅在这个应用中要求使用的jar文件,如数据库驱动jar文件
    /WEB-INF/src/：源码目录，按照包名结构放置各个java文件。
    /WEB-INF/database.properties：数据库配置文件

利用方法

通过找到web.xml文件，推断class文件的路径，最后直接class文件，在通过反编译class文件，得到网站源码。
.DS_Store文件泄漏
测试

    http://www.example.com/.ds_store

利用工具

ds_store_exp
.hg源码泄漏
测试

http://www.example.com/.hg/
利用工具

dvcs-ripper

#############################
分布式版本控制系统(git)源码泄漏
    .git
    README.MD
        .gitignore
集中式版本控制系统(svn)源码泄漏
    .svn
#############################
VIM编辑器
    备份文件 : 
        *.*~
    异常退出备份文件 : 
        .*.*.swp
        .*.*.swo
        .*.*.swn
        .*.*.swm
        .*.*.swl
    日志文件 : 
        _viminfo
        .viminfo
#############################
Emacs编辑器
    *.*~
    *.*~1~
    *.*~2~
    *.*~3~
#############################
nano编辑器
    *.*.save
    *.*.save1
    *.*.save2
    *.*.save3
#############################
Editplus编辑器
    *.*.bak_Edietplus
#############################
其他编辑器
    *.*.bak
    *.*.back
#############################
开发人员测试失误遗留文件
    phpinfo.php
    test.php

#############################
Bash命令历史记录
    .bash_history
#############################
网站备份压缩
.rar
.zip
.7z
.tar.gz
.bak


