from pathlib import Path


APPS_PATH = Path('my-dir-path')


def latest_modified_file(paths):
    mtimes_n_paths = []
    for path in paths:
        mtime = path.stat().st_mtime
        mtimes_n_paths.append((mtime, path))
    latter = sorted(mtimes_n_paths)[-1]
    return latter[1]


def path_to_smodule(path):
    module = path.name[:-3]
    appsdir = path.parent.parent.name
    appdir = path.parent.name
    return f'{appsdir}.{appdir}.{module}'


def main():
    option = 1
    option_path_map = {}
    for item in sorted(conf.APPS.iterdir()):
        if item.is_dir():
            # print(item.name)
            for subitem in sorted(item.iterdir()):
                if subitem.is_file() and subitem.suffix == '.py':
                    print(f'{option}: {subitem.name}')
                    option_path_map[option] = subitem
                    option += 1
    print()
    latest = latest_modified_file(option_path_map.values())
    print(f'l: {latest} (latest modified file)')
    print()
    choice = input('Choose: ')
    if choice == 'l':
        path = latest
    elif choice.isdigit():
        path = option_path_map[int(choice)]
    else:
        return
    smodule = path_to_smodule(path)
    app = __import__(smodule, fromlist=[APPS.name])
    app.main()


main()
