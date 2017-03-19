使用方法
命令行方式

（提示：如果你尚未安装 MyQR ，以下内容请使用python(3) myqr.py 而非myqr 。）

# 概括
myqr 	Words
		[-v {1,2,3,...,40}]
		[-l {L,M,Q,H}]
        [-n output-filename]
		[-d output-directory]
		[-p picture_file]
		[-c]
		[-con contrast]
		[-bri brightness]

    普通二维码 介绍了 Words, -v, -l, -n, -d
    艺术二维码 介绍了 -p, -c, -con, -bri
    动态GIF二维码 介绍了动态的生成方法和注意点

普通二维码

#1 Words
myqr https://github.com

    在命令后输入链接或者句子作为参数，然后在程序的当前目录中产生相应的二维码图片文件，默认命名为” qrcode.png“。

    ​

#2 -v, -l
myqr https://github.com -v 10 -l Q

    默认边长是取决于你输入的信息的长度和使用的纠错等级；

    而默认纠错等级是最高级的H。

    自定义：如果想要控制边长和纠错水平就使用 -v 和 -l 参数。

    -v 控制边长，范围是1至40，数字越大边长越大；

    -l 控制纠错水平，范围是L、M、Q、H，从左到右依次升高。

#3 -n, -d
myqr https://github.com -n github_qr.jpg  -d .../paths/

    默认输出文件名是“ qrcode.png "，而默认存储位置是当前目录。

    自定义：可以自己定义输出名称和位置。注意同名文件会覆盖旧的。

    -n 控制文件名，格式可以是 .jpg， .png ，.bmp ，.gif ；

    -d 控制位置。

    ​

艺术二维码

#1 -p
myqr https://github.com -p github.jpg

    参数-p 用来将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片。

    ​

#2 -c
myqr https://github.com -p github.jpg -c

    加上参数 -c 可以使产生的图片由黑白变为彩色的。

    ​

#3 -con, -bri
myqr https://github.com -p github.jpg [-c] -con 1.5 -bri 1.6

    参数-con 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。

    参数 -bri 用来调节图片的亮度，其余用法和取值与 -con 相同。

动态GIF二维码

动态二维码与上述的带图片的二维码的生成方法没什么区别，你只要采用 .gif 格式的图片即可生成黑白或者彩色的动态二维码。但注意如果使用了 -n 参数自定义输出的文件名，切记其格式也必须是 .gif 格式。
作为导入文件

# 安装模块后
from MyQR import myqr
version, level, qr_name = myqr.run(
	words,
    version=1,
    level='H',
    picture=None,
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name=None,
    save_dir=os.getcwd()
	)

以下各个参数已经在上文有所介绍

# help(myqr)
Positional parameter
   words: str

Optional parameters
   version: int, from 1 to 40
   level: str, just one of ('L','M','Q','H')
   picutre: str, a filename of a image
   colorized: bool
   constrast: float
   brightness: float
   save_name: str, the output filename like 'example.png'
   save_dir: str, the output directory

使用提示

    请采用正方形或近似正方形的图片

    建议在图片尺寸大的时候使用 -v 的值也应该适当变大。

    如果图片有透明无色部分，最终效果是：

    你可以将透明部分修改成白色，最终效果会变成

可用字符

    数字 0 到 9

    大小写的英文字母

    常用英文标点符号和空格

    · , . : ; + - * / \ ~ ! @ # $ % ^ & ` ' = < > [ ] ( ) ? _ { } | and  (space)

