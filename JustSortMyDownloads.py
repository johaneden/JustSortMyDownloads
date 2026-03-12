import pathlib
import json

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


config_file = dict()

placeholders = {
    'home': str(pathlib.Path.home()),
    'script_dir': pathlib.Path(__file__).parent
}


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

try:
    with open(placeholders['script_dir'] / 'paths_config.json', 'r') as data:
        config_file = json.load(data)
except:
    print('Config file doesn\'t exist')


unsorted_folders = list()

for folder in config_file.get('unsorted_folders', [placeholders['home']+'/Downloads']):
    folder = folder.replace('{home}',placeholders['home'])
    unsorted_folders.append(pathlib.Path(folder))
print(unsorted_folders)





files_dir = config_file.get(pathlib.Path('path'), pathlib.Path(placeholders['home']) / 'Downloads' / 'sorted files')

files_dir.mkdir(exist_ok=True)

for path in list(dirs.keys()) + ['etc']:
    tmp = files_dir / path
    tmp.mkdir(exist_ok=True)



for folder in unsorted_folders:
    files = [el for el in folder.iterdir() if el.is_file()]
    print(f'Unsorted files: {len(files)}')
    for file in files:
        for key, value in dirs.items():
            if file.suffix in value:
                original_name = name_check(files_dir / key / file.name)
                print(f'{original_name.name} moved in {key}')
                file.move(files_dir / key / original_name.name)
                break
        else:
            original_name = name_check(files_dir / 'etc' / file.name)
            file.move(files_dir / 'etc' / original_name.name)
            print(f'{original_name.name} moved in etc.')

    print(f'{folder.name} sorted.'.upper())

input("Press Enter to exit...")

