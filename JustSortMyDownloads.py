import pathlib

def name_check(target_path: pathlib.Path):
    if not target_path.exists():
        return target_path
    counter = 1
    old_file_name =  pathlib.Path(f'{target_path.stem}{target_path.suffix}')
    while target_path.exists():
        file_name =  pathlib.Path(f'{old_file_name.stem} ({counter}){old_file_name.suffix}')
        target_path = target_path.parent / file_name
        counter += 1
    return target_path


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
            original_name = name_check(files_dir / key / file.name)
            file.move(files_dir / key / original_name.name)
            print(f'{original_name} moved in {key}')
            break
    else:
        original_name = name_check(files_dir / 'etc' / file.name)
        file.move(files_dir / 'etc' / original_name.name)
        print(f'{original_name} moved in etc dir.')
else:
    print('Sorting completed.')

input("Press Enter to exit...")



















