import os
from pathlib import Path
from PIL import Image

def tif_to_jpeg(folder_input, folder_to):
    if os.path.exists(folder_input) == False:
        return f'Path does not exist: {folder_input}'

    if os.path.isdir(folder_input) == False:
        return f'Path is not a directory: {folder_input}'

    files = Path(folder_input).glob('*.tif')

    len_files = len(list(files))
    if len_files == 0:
        return f'There are no .tif files in the path: {folder_input}'

    if os.path.exists(folder_to) == False:
        os.makedirs(folder_to)

    loaded = 0
    for file in files:
        full_name = os.path.basename(file)
        name = os.path.splitext(full_name)[0]
        full_path_input = os.path.join(folder_input, full_name)
        full_path_out = os.path.join(folder_to, name + '.jpeg')

        try:      
            im = Image.open(full_path_input)
            im.save(full_path_out, 'JPEG')
            print(f'Loaded: {full_path_out}')
            loaded += 1
        except Exception as ex:
            return f'{ex}: {full_path_input}'

    print()
    return f'Images saved successfully \nLoaded: {loaded}/{len_files} \nPath: {folder_to}'


if __name__ == '__main__':
    paths = input('From/To: ').strip().split()
    print()
    print(tif_to_jpeg(paths[0], paths[1]))
