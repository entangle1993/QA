# Mac命令  
(两个空格md换行)  
打开某个隐藏文件夹：open /usr/bin  
寻找某个名字的文件：sudo find / -iname ‘chromedriver'  
查看rootless（系统默认将会锁定 /system /sbin /usr 这三个目录）状态：csrutil status  
防止 .DS_Store 文件的生成: defaults write com.apple.desktopservices DSDontWriteNetworkStores true  
Thumbs.db是一个用于Microsoft Windows XP或mac os x缓存Windows Explorer的缩略图的文件。

软件有经过了汉化或者破解，所以可能被Mac认为「已损坏」
$ sudo spctl --master-disable 即可~

export 查看当前环境变量