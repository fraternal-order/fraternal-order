import urllib.request
import sys
import re
import os
 
w = 0
wt = 0
 
 
class Dowsong():  # 下载歌曲
    def __init__(self, songid):
        self.songid = songid
        """获取歌名"""
        name = urllib.request.urlopen('https://music.163.com/song?id=' + self.songid).read().decode()  # 获取源码
        name = re.compile('"title": "' + "(.*?)" + '",', re.S).findall(name)  # 获取歌名
        print('正在下载' + name[0])
        if os.path.exists(f + '/' + name[0] + '.mp3') == True:  # 判断该文件是否存在，如果存在就删除
            os.remove(f + '/' + name[0] + '.mp3')
        dow = 'http://music.163.com/song/media/outer/url?id=' + self.songid + '.mp3'  # 下载api
        urllib.request.urlretrieve(dow, f + '/' + name[0] + '.mp3')  # 下载
        kb = ((os.path.getsize(f + '/' + name[0] + '.mp3')) / 1000)  # 计算大小
        if (kb) < 100:  # 判断是否下载成功
            print(name[0] + '下载失败')
            os.remove(f + '/' + name[0] + '.mp3')
            w = +1
        else:
            print(name[0] + '下载成功' + '文件大小为' + str(kb) + 'kb')
            wt = +1
 
 
i = input('请输入歌曲连接或歌单连接')
# 类型判断
t = ''
d = ''
try:  # 判断是否包含song
    a = re.search('song', i).span()
except:
    t = '0'
else:
    d = 'song'
    print('你输入的可能为歌曲')
if t == '0':
    try:
        a = re.search('playlist', i).span()  # 判断是否包含playlist
    except:
        print('你输入的可能不是歌曲或者歌单的连接')
        sys.exit()
    else:
        d = 'playlist'
        print('你输入的可能是歌单')
i = i.split('id=')  # 截取id
i = i[1]
i = i.replace('&user', '', )
f = input('请输入要保存到的文件目录：')
 
try:
    os.makedirs(f)  # 如果目录不存在那就创建个
except:
    pass
 
print(i)
# 处理歌曲
if d == 'song':
    Dowsong(i)
# 处理歌单、
if d == 'playlist':
    url = 'https://music.163.com/playlist?id=' + i
    url = urllib.request.urlopen(url).read().decode()  # 获取歌单源码
    names = re.compile('"title": "' + "(.*?)" + '",', re.S).findall(url)  # 取歌单名
    print('当前歌单名:' + names[0])
    url = re.compile(
        '<span class="f-ff2">歌曲列表</span>' + "(.*?)" + '<textarea id="song-list-pre-data" style="display:none;">',
        re.S).findall(url)  # 截取中间信息
    url = url[0]
    url = re.compile('<li><a href="/song' + "(.*?)" + '">', re.S).findall(url)  # 获取歌曲id
    print('获取到' + str(len(url)) + '个音乐id信息')
    f = f + '/' + names[0]  # 以歌单名，创建文件目录
    try:
        os.makedirs(f)
    except:
        pass
    for urls in url:
        urls = urls.replace('?id=', '', )
        Dowsong(urls)
    print('下载成功' + str(wt) + '个' + '\n' + '下载失败' + str(w))
