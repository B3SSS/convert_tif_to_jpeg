# Function to convert .TIF to .JPEG

Устанавливаем библиотеку __Pillow__ (version: __9.5.0.__).
Для этого в терминале вводим команду:
```
pip install pillow==9.5.0
```

Импортируем библиотеки, необходимые для работы:
```python
from pathlib import Path
from PIL import Image
import os
```

Сама функция выглядит следующим образом:
```python
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
```

C помощью начальных условий проверяем, существует ли путь, из которого требуется брать файлы с __TIF__ расширением, и является ли он директорией (__не файлом__):
```python
if os.path.exists(folder_input) == False:
        return f'Path does not exist: {folder_input}'

if os.path.isdir(folder_input) == False:
        return f'Path is not a directory: {folder_input}'
```

Если путь корректный, то запрашиваем все файлы с расширением __TIF__, которые находятся там: 
```python
files = Path(folder_input).glob('*.tif')
```

Проверяем, есть ли хоть один файл с расширением __TIF__ в данной директории:
```python
len_files = len(list(files))
if len_files == 0:
    return f'There are no .tif files in the path: {folder_input}'
```

Проверка существования директории, в которую будут загружены файлы с расширением __JPEG__. Если данной директории не существует, создаем со всеми промежуточными директориями:
```python
if os.path.exists(folder_to) == False:
        os.makedirs(folder_to)
```

И наконец, перебирая все файлы с расширением __TIF__, проходит загрузка файлов с тем же названием по другому пути:
```python
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
```
В конце функция выводит сообщение об успешной загрузке файлов с __JPEG__ расширением, их количестве и пути, по которому проходила загрузка:
```python
return f'Images saved successfully \nLoaded: {loaded}/{len_files} \nPath: {folder_to}'
```

При запуске программы запрашиваем у пользователя пути (откуда/куда) и вызываем саму функцию:
```python
if __name__ == '__main__':
    paths = input('Paths: ').strip().split()
    print()
    print(tif_to_jpeg(paths[0], paths[1]))
```
