from os import path
import os
from pathlib import Path
from PIL import Image

def tif_to_jpeg(folder_input, folder_to):
    if os.path.exists(folder_input) == False:
        return f'Path does not exist: {folder_input}'

    if os.path.isdir(folder_input) == False:
        return f'Path is not a directory: {folder_input}'

    files = Path(folder_input).glob('*.tif')

    result = 0

    for _ in files:
        result += 1

    if result == 0:
        return f'There are no .tif files in the path: {folder_input}'

    if os.path.exists(folder_to) == False:
        os.makedirs(folder_to)

    num = 0
    files = Path(folder_input).glob('*.tif')
    for file in files:
        full_name = path.basename(file)
        name = path.splitext(full_name)[0]
        full_path_input = folder_input + '\\' + full_name
        full_path_out = folder_to + '\\' + name + '.jpeg'

        try:      
            im = Image.open(full_path_input)
            im.save(full_path_out, 'JPEG')
            num += 1
        except Exception as ex:
            return f'{ex}: {full_path_input}'

    return f'All images saved successfully \nLoaded: {num}/{result} \nPath: {folder_to}'


if __name__ == '__main__':
    folder_input = input('Start folder: ')
    folder_to = input('Destination folder: ')
    print()
    print(tif_to_jpeg(folder_input, folder_to))
