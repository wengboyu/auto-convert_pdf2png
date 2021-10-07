import fitz
from os import walk, mkdir, getcwd
from os import path as Path

def tran2image(filepath, zoom=4):
    mat = fitz.Matrix(zoom, zoom)
    filedir, filename = Path.split(filepath)[0], Path.split(filepath)[1].replace('.pdf', '')
    try:
        doc = fitz.open(filepath)
    except:
        return print('{state:>4}, {name}'.format(state='fail', name=filename))
    try:
        mkdir(filedir + '\\' + filename)
    except:
        pass
    for page in doc:
        pix = page.get_pixmap(matrix=mat)
        pix.save(r'{filedir}\{filename}\{number}.png'.format(
            filedir=filedir, filename=filename, number=page.number))
    return print('{state:>8}, {name}'.format(state='finish', name=filename))

if __name__ == '__main__':
    while True:
        try:
            zoom = input('''Please input how many times built-in (72) DPI:''')
            zoom = int(4) if zoom == '' else float(zoom)
            break
        except:
            print('''Please input a number or just press enter''')
            continue
    current_dir = Path.abspath(getcwd())
    files_name = []
    for (dirpath, dirname, filenames) in walk(current_dir):
        for filename in filenames:
            if ('.pdf' in filename):
                files_name.append(filename)
    print('Processing, please wait')
    for name in files_name:
        filepath = current_dir + '\\' + name
        tran2image(filepath, zoom)
    input("\nPress Enter To Exit...")