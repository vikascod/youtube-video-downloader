from pytube import YouTube


link = "https://www.youtube.com/watch?v=nqye02H_H6I"
video = YouTube(link)
# print(video.title)

videos = video.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Enter : "))
videos[strm].download()
print('Seccessful')