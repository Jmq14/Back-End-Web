# ConvMusic Website

## 服务器登录
在Teminal/cmd中用ssh登录服务器

`ssh chenlr@chenlr.com -p 510`

或者

`ssh chenlr@104.131.0.194 -p 510`

## 服务器git使用
中期检查前的所有代码在文件夹`convmusic`中，git仓库同步在文件夹`Back-End-Web`中。

将更新的代码从本地clone来的仓库提交到本远程仓库（参看 http://rogerdudler.github.io/git-guide/index.zh.html，基本上就是make some change -> `git add` (添加新建的文件，图形界面可省掉这一步) -> `git commit -m "这次提交的标题"` -> `git push`）。

然后登录服务器，在`Back-End-Web`文件夹目录下输入命令`git pull original master`便能更新到最新的master库内容。

若想要切换到自己的分支运行自己那部分的代码，同样在`Back-End-Web`文件夹目录下输入命令`git checkout 你的分支名`，然后再`git pull`。

禁止直接在服务器上更改`Back-End-Web`的内容！（改了也保存不了下次pull还是会被覆盖QAQ）
