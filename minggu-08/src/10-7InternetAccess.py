from urllib.request import urlopen
#url contoh di dokumentasi sudah expired
with urlopen('https://www.timeanddate.com/worldclock/indonesia/yogyakarta') as response:
    for line in response:
        line = line.decode('utf-8')
        if 'WIB' in line or 'EDT' in line:
            print(line)
