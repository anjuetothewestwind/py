def make_album(singer,name,song_num=-1):
    if song_num== -1:
        return {"singer":singer,"name":name}
    else:
        return {"singer":singer,"name":name,'song_num' : song_num}
    
A = make_album("taylor","you belong with me.",12)
B = make_album("backsteetboy","the west")
C = make_album('fenghuangchuanqi','yueliangzhishang')
print(A)
print(B)
print(C)
while True:
    print('please tell me the singer and the album name.')
    print("press 'q' to exit.")
    singer = input('singer name please:')
    if singer == 'q':break
    album_name = input("album name please:")
    if album_name == 'q':break
    print(make_album(singer,album_name))