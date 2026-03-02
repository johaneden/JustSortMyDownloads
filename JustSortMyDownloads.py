import pathlib
dirs = {
    # pic
    'photo': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff', '.psd'],

    # docs
    'documents': ['.txt', '.md', '.pdf', '.doc', '.docx', '.odt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],


    # audio
    'music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],

    # video
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],

    # torrent
    'torrent': ['.torrent'],

    # # exe
    # 'executables': ['.exe', '.msi', '.bat', '.sh', '.app', '.deb', '.rpm', '.dmg'],

    # # code
    # 'code': ['.py', '.js', '.html', '.css', '.cpp', '.c', '.h', '.java', '.php', '.rb', '.go', '.swift', '.json', '.xml', '.yaml', '.toml']


}


directory = pathlib.Path.home() / "Downloads"
files_dir = directory / 'sorted files'
files_dir.mkdir(exist_ok=True)
for path in dirs.keys():
    tmp = files_dir / path
    tmp.mkdir(exist_ok=True)
tmp = files_dir / 'etc'
tmp.mkdir(exist_ok=True)


files = [el for el in directory.iterdir() if el.is_file()]
print(f'Unsorted files: {len(files)}')
for file in files:
    for key, value in dirs.items():
        if file.suffix in value:
            file.move(files_dir / key / file.name)
            print(f'{file.name} moved in {key}')
            break
    else:
        print(f'{file.name} moved in etc dir.')
        file.move(files_dir / 'etc' / file.name)
else:
    print('Sorting completed.')

input("Press Enter to exit...")



















