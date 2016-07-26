
import requests
import urllib
import re
import codecs

# 榜单歌曲批量下载
# r = requests.get('http://music.163.com/api/playlist/detail?id=2884035')  # 网易原创歌曲榜
# r = requests.get('http://music.163.com/api/playlist/detail?id=19723756') # 云音乐飙升榜
# r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')  # 云音乐热歌榜
r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')    # 云音乐新歌榜

# 歌单歌曲批量下载
# r = requests.get('http://music.163.com/api/playlist/detail?id=123415635')    # 云音乐歌单——【华语】中国风的韵律，中国人的印记
# r = requests.get('http://music.163.com/api/playlist/detail?id=122732380')    # 云音乐歌单——那不是爱，只是寂寞说的谎

arr = r.json()['result']['tracks'] # 共有100首歌

for i in range(63, 100):    # 输入要下载音乐的数量，1到100。

	name = arr[i]['name'] # 歌曲名称
	link = arr[i]['mp3Url']
	urllib.request.urlretrieve(link, '网易云音乐\\' + name + '.mp3') # 下载歌曲（提前要创建文件夹

	link = arr[i]['album']['blurPicUrl'];
	urllib.request.urlretrieve(link, '网易云音乐\\' + name + '.jpg') # 下载专辑图片

	musicId = str(arr[i]['id'])
	l = requests.get('http://music.163.com/api/song/lyric?os=pc&id='\
		+ musicId + '&lv=-1&kv=-1&tv=-1') # 对应歌曲的歌词
	lyric = '本歌曲未有歌词'
	if 'lrc' in l.json().keys():
		lyric = l.json()['lrc']['lyric']
		temp = re.compile(r'\[.*?\]')
		lyric = temp.sub('', lyric) # 用正则表达式清除歌词前的时间信息
	info = name + '.txt' # 存放歌曲信息的文件
	f = codecs.open('网易云音乐\\' + info, 'w', 'utf-8')
	f.writelines(name + '\n')
	f.writelines('演唱者：' + arr[i]['artists'][0]['name'] + '\n') # 写入演唱者
	f.writelines(lyric)
	f.close();
	print(name + ' 下载完成')