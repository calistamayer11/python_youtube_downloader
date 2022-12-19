from pytube import YouTube


link = input('Please add your YouTube link\n')
YouTube(link).streams.filter(file_extension='mp4', res="720p").first().download()