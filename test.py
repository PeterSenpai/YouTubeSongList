with open('song.txt', encoding='UTF-8') as f:
    keywords = f.readlines()

keywords = [k.strip() for k in keywords]

print(keywords)