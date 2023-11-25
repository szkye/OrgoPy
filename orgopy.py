import os
from pathlib import Path

home = Path.home()


def check_for_dirs():

    global images_dir
    images_dir = Path(home, "Downloads", "IMAGES")

    global files_dir
    files_dir = Path(home, "Downloads", "FILES")

    global apps_dir
    apps_dir = Path(home, "Downloads", "APPS")

    global misc_dir
    misc_dir = Path(home, "Downloads", "MISC")

    global music_dir
    music_dir = Path(home, "Downloads", "MUSIC")

    if not images_dir.exists():
        os.mkdir(images_dir)
    else:
        print("Images folder already exists.")

    if not files_dir.exists():
        os.mkdir(files_dir)
    else:
        print("Files folder already exists.")

    if not apps_dir.exists():
        os.mkdir(apps_dir)
    else:
        print("Apps folder already exists.")

    if not misc_dir.exists():
        os.mkdir(misc_dir)
    else:
        print("Misc folder already exists.")

    if not music_dir.exists():
        os.mkdir(music_dir)
    else:
        print("All here")


def move_by_type():

    downloads_dir = Path(home, "Downloads")
    apps_suffix = ['.exe', '.sh', '.bat', '.run', '.apk', '.cmd', '.x86', '.x86_64', '.app']    
    music_suffix = ['.mp3', '.flac', '.asd', '.ogg', '.wav', '.wave', '.wma', '.aac']
    files_suffix = ['.txt', '.torrent', '.html', '.iso', '.bin']
    image_suffix = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico',
                    '.jfif', '.pjpeg', '.pjp', '.ai', '.eps', '.raw', '.indd', '.psd', '.pdf',
                    '.xcf', '.dng', '.heif', '.jpe']
    total_suffix = apps_suffix + music_suffix + files_suffix + image_suffix

    for x in downloads_dir.iterdir():
        if x.is_file():
            if x.name == 'desktop.ini':
                continue
            if x.suffix in music_suffix:
                print(f'Moved {x.name} to {music_dir}.')
                os.replace(downloads_dir/x.name, music_dir/x.name)
                continue
            if x.suffix in apps_suffix:
                print(f'Moved {x.name} to {apps_dir}.')
                os.replace(downloads_dir/x.name, apps_dir/x.name)
                continue
            if x.suffix in files_suffix:
                print(f'moved {x.name} to {files_dir}.')
                os.replace(downloads_dir/x.name, files_dir/x.name)
                continue
            if x.suffix in image_suffix:
                print(f'moved {x.name} to {images_dir}.')
                os.replace(downloads_dir/x.name, images_dir/x.name)
                continue
            if x not in total_suffix:
                print(f'moved {x.name} to {misc_dir}.')
                os.replace(downloads_dir/x.name, misc_dir/x.name)
                continue


check_for_dirs()
move_by_type()
