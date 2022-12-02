from commons import trails

def main():
    filenames = trails.filter_filenames('apps', '', 'py')
    app_names = [i[:i.find('.py')] for i in filenames]
    for option, name in enumerate(app_names, start=1):
        print(f'[{option}] {name}')
    print()
    choice = input('Choose: ')
    if not choice.isdigit():
        return
    app_name = app_names[int(choice)-1]
    app = __import__(f'apps.{app_name}', fromlist=['apps'])
    app.main()

main()
