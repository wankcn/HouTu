创建的项目之后，Cocos Creator会自动的创建出以下的文件夹结构
```
ProjectName
├──assets
├──library
├──local
├──packages
├──settings
├──temp
└──project.json
```

# 1.assets
资源文件夹，放置游戏中所有的本地资源，脚本和第三方库文件。
assets每个资源导入的时候都会生成一个`.meta`的文件，用于存储资源倒入后的信息和其他资源关联，是描述性文件。

# 2.library
它是assets中的资源导入后自动生成的，会把文件的结构和资源的格式处理成最终游戏发布时需要的形式。就算删除也会根据资源重新生成该文件夹。

# 3.local
项目的本地设置，主要包含面板布局，窗口大小位置，位置信息等。

# 4.setting
也使一些配置文件，保存项目相关的设置，如 构建发布 菜单里的包名、场景和平台选择等，需要和项目一起进行版本控制。

# 5.<font color='red'>project.json</font>
存在根目录下。`project.json` 文件和`assets` 文件夹一起，作为验证Cocos Creator项目合法性的标志。只有包含了这两个内容的文件夹才能被作为Cocos Creator项目打开，需要纳入版本控制中。

# 6.packages
扩展文件夹，存放项目的扩展插件等。

# 7.Temp
是一个临时文件夹，用于缓存Cocos Creator在本地的临时文件，当项目关闭时会自动删除。

# 8.build
使用项目--构建发布。通过构建发布可以把游戏最终发布到不同的平台里面。构建运行就会产生build文件夹。

# 9.Git
Cocos Creator新建项目时，会自动生成 .gitignore 文件，用于排除不应该提交到 git 仓库的文件。只需要提交 assets、packages、settings、project.json，或其它手动添加的关联文件。