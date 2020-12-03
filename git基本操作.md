# 上传到git
1.在远程创建仓库
2.创建本地仓库并配置`.gitignore`上传忽略文件
```
git init                           // 初始化git仓库
git add .                          // 提交所有的文件
git commit -m xxxx                 // 暂存区的代码提交到远程仓库  xxx写提交说明
git remote add origin xxx          // 连接远程仓库 xxx为远程仓库git地址
git push -u origin master          // 第一次本地仓库推送到远程仓库
```

# 查询操作记录
```
git status                         // 查看当前项目的状态
git log                            // 查看之前提交的记录
git log --author='wankcn'          // 查看某人提交的代码 若无显示 表明未提交代码或没author这个人
```

# 配置用户名和邮箱
`git config --global`是指全局配置
```
git config --global user.name 'xxx'           // 配置用户名
git config --global user.name 'xx@xx.com'     // 配置邮箱
git config --global --list                    // 检查当前配置的用户名和邮箱是否成功
```

# 修改或新增项目中的文件
```
git add xxx xxx                   // 本地文件添加到暂存区 多个文件之间用空格隔开
git commit -m xxx                 // 将修改的文件添加到远程仓库
```

# 删除文件
**1. 手动删除文件**

在文件夹中删除文件以后执行以下命令
```
git add .                          // 先把删除后剩余的所有文件提交到暂存区
git commit -m xxx                  // 提交到远程仓库并注释
```
**2. 命令行删除文件**
```
git rm xxx                         // 删除xxx文件
git add .                          // 剩余文件加到暂存区
git commit -m xxx                  // 提交到远程仓库并注释
```

# 文件重命名
**1. 手动重命名文件**
假设工程里有一个文件 `111.txt`被改成了`222.txt`，执行下面的命令
```
git add 222.txt
git rm 111.txt
git commit -m xxx                  // 提交到远程仓库并注释
```
**2. 命令行重命名文件**
假设把文件 `333.txt`被改成了`444.txt`
```
git mv 333.txt 444.txt             // 先改动之前的名字 后改动之后的名字
git commit -m xxx                  // 提交到远程仓库并注释
```

# 移动文件
**1.使用重命名来移动文件**
将文件`111.txt`移动到文件夹`files`中
```
git mv 111.txt files               // 移动的文件 移动的位置
git commit -m xxx                  // 提交到远程仓库并注释
```
**2.移动文件并重命名**
将文件`111.txt`移动到文件夹`files`中并重命名为`222.txt`
```
git mv 111.txt files/222.txt       // 移动的文件 移动的位置/重命名
git commit -m xxx                  // 提交到远程仓库并注释
```