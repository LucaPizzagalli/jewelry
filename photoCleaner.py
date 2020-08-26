from glob import glob
from pathlib import Path
from shutil import copyfile
from PIL import Image

mapping = {
    'number-view': {
        '1': 'oblique',
        '2': 'box',
        '3': 'front',
        '4': 'side',
        '5': 'back',
        '6': 'under',
        'a': 'model1',
        'b': 'model2',
        'c': 'model3',
        'd': 'model4',
        'e': 'model5',
    },
    'number-number': {
        '1': '1',
        '2': '2',
        '3': '4',
        '4': '5',
        '5': '6',
        '6': '7',
        'a': '3a',
        'b': '3b',
        'c': '3c',
        'd': '3d',
        'e': '3e',
    },
    'diameter-x': {
        '012': '1',
        '014': '2',
        '020': '4',
        '030': '5',
    },
    'view-sizes': {
        'box': [1000, 1000],
        'oblique': [1000, 1000],
        'front': [1000, 1000],
        'side': [1000, 1000],
        'back': [1000, 1000],
        'under': [1000, 1000],
        'model1': [1000, 1000],
        'model2': [1000, 1000],
        'model3': [1000, 1000],
        'model4': [1000, 1000],
        'model5': [1000, 1000],
        'combo': [1000, 1000],
    },
    'color-color': {
        'OG': 'yellow',
        'OR': 'pink',
        'RU': 'black',
        'RB': 'white',
    },
    'type-type': {
        'AC': 'anello-argento-padelli-silver-ring',
    }
}


def main():
    clean_items_photos()
    clean_combos_photos()


def clean_combos_photos():
    existent_items = [path.split('/')[-2] for path in glob('./Data/CleanPhotos/Items/*/')]
    combo_paths = glob('./Data/RawPhotos/Combo/*')
    for photo_path in combo_paths:
        name = photo_path.split('/')[-1].split('.')[0]
        items = []
        if name[0:2] != 'AC':
            print('Warining nome sconosciuto a: ' + photo_path)
            continue

        if name[2:5] == '___':
            for diameter in mapping['diameter-x'].keys():
                items.append('AC' + diameter)
        elif name[2:5] not in mapping['diameter-x'].keys():
            print('Warining nome sconosciuto b: ' + photo_path)
            continue
        else:
            items.append('AC' + name[2:5])

        if name[5:7] == '__':
            new_items = []
            for item in items:
                for color in mapping['color-color'].keys():
                    new_items.append(item + color)
            items = new_items
        elif name[5:7] not in mapping['color-color'].keys():
            print('Warining nome sconosciuto c: ' + photo_path)
            continue
        else:
            for index, item in enumerate(items):
                items[index] = item + name[5:7]

        for item in items:
            if item in existent_items:
                with Image.open(photo_path) as image:
                    image = image.resize((mapping['view-sizes']['combo'][0], mapping['view-sizes']['combo'][1]))
                    image.save('./Data/CleanPhotos/Marco/' + item + '/' + name + '.jpg')


def clean_items_photos():
    photo = {'items': {}}
    item_paths = glob('./Data/RawPhotos/Items/*/')
    for item_path in item_paths:
        item = item_path.split('/')[-2]
        photo['items'][item] = {}
        photo_paths = glob(item_path + '*')
        Path('./Data/CleanPhotos/Items/' + item).mkdir(parents=True, exist_ok=True)
        Path('./Data/CleanPhotos/Marco/' + item).mkdir(parents=True, exist_ok=True)

        for photo_path in photo_paths:
            name = photo_path.split('/')[-1].split('.')[0]
            if name not in mapping['number-view'].keys():
                print('Warining nome sconosciuto: ' + photo_path)
                continue
                # raise Exception('LUCAERROR: nome sconosciuto: ' + photo_path)
            view = mapping['number-view'][name]
            number = mapping['number-number'][name]
            new_name = '{number}-bottega-orafa-ISella-{type}-{diameter}-{color}-{view}.jpg'.format(
                number=number,
                type=mapping['type-type'][item[:2]],
                diameter=item[2:5],
                color=mapping['color-color'][item[-2:]],
                view=view
            )
            photo['items'][item][view] = {'old_path': photo_path, 'name': new_name}
            
            with Image.open(photo_path) as image:
                print(photo_path)
                image = image.resize((mapping['view-sizes'][view][0], mapping['view-sizes'][view][1]))
                image.save('./Data/CleanPhotos/Marco/' + item + '/' + new_name)
                image.save('./Data/CleanPhotos/Items/' + new_name)
    # print(photo)


if __name__ == '__main__':
    main()
