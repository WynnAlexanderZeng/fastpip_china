import click
import os

mirrors = {"清华":"https://pypi.tuna.tsinghua.edu.cn/simple ",
           "阿里云":"http://mirrors.aliyun.com/pypi/simple ",
           "中科大":"https://pypi.mirrors.ustc.edu.cn/simple ",
           "豆瓣":"http://pypi.douban.com/simple "
           }

@click.command()
@click.option('--image','-i', default='中科大', help='Used image, the default image is China University of science and technology, including Tsinghua, ADrive, China University of science and technology, Douban, and the official pypi\n使用的映像，默认映像是中国科技大学的，映像包括清华、阿里云、中国科技大学、豆瓣和官方pypi')
@click.option('--package','-p',default='防错误123123kdfhhiuqehdhkfhgfy1gfa', help='Package you want to download\n你要下载的包')
def fpip(image,package):
    '''Quickly download pypi packages in China (the principle is to use images)
    在中国快速下载pypi的包（原理是使用映像）'''
    click.echo(str(image))
    click.echo(str(package))
    os.system("pip3 install -i "+ mirrors[str(image)] + str(package))
    os.system("py -m pip3 install -i "+ mirrors[str(image)] + str(package))
if __name__ == '__main__':
    fpip()
    
