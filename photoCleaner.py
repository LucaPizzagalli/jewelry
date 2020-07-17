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
        'model1': [1555, 1036],
        'model2': [1555, 1036],
        'model3': [1555, 1036],
        'model4': [1555, 1036],
        'model5': [1555, 1036],
        'combo': [1000, 1000],
    },
    'color-color': {
        'OG': 'yellow-gold',
        'OR': 'pink-gold',
        'RU': 'black-gold',
        'RB': 'white-gold',
    }
}


def main():
    clean_items_photos()
    clean_combos_photos()


def clean_combos_photos():
    existent_models = [path.split('/')[-2] for path in glob('./Data/CleanPhotos/Models/*/')]
    combo_paths = glob('./Data/RawPhotos/Combo/*')
    for photo_path in combo_paths:
        name = photo_path.split('/')[-1].split('.')[0]
        models = []
        if name[0:2] != 'AC':
            print('Warining nome sconosciuto a: ' + photo_path)
            continue

        if name[2:5] == '___':
            for diameter in mapping['diameter-x'].keys():
                models.append('AC' + diameter)
        elif name[2:5] not in mapping['diameter-x'].keys():
            print('Warining nome sconosciuto b: ' + photo_path)
            continue
        else:
            models.append('AC' + name[2:5])

        if name[5:7] == '__':
            new_models = []
            for model in models:
                for color in mapping['color-color'].keys():
                    new_models.append(model + color)
            models = new_models
        elif name[5:7] not in mapping['color-color'].keys():
            print('Warining nome sconosciuto c: ' + photo_path)
            continue
        else:
            for index, model in enumerate(models):
                models[index] = model + name[5:7]

        for model in models:
            if model in existent_models:
                with Image.open(photo_path) as image:
                    image = image.resize((mapping['view-sizes']['combo'][0], mapping['view-sizes']['combo'][1]))
                    image.save('./Data/CleanPhotos/Models/' + model + '/' + name + '.jpg')

def clean_items_photos():
    photo = {'models': {}}
    model_paths = glob('./Data/RawPhotos/Models/*/')
    for model_path in model_paths:
        model = model_path.split('/')[-2]
        photo['models'][model] = {}
        photo_paths = glob(model_path + '*')
        Path('./Data/CleanPhotos/Models/' + model).mkdir(parents=True, exist_ok=True)

        for photo_path in photo_paths:
            name = photo_path.split('/')[-1].split('.')[0]
            if name not in mapping['number-view'].keys():
                print('Warining nome sconosciuto: ' + photo_path)
                continue
                # raise Exception('LUCAERROR: nome sconosciuto: ' + photo_path)
            view = mapping['number-view'][name]
            number = mapping['number-number'][name]
            new_name = number + '-silver-ring-' + model[2:5] + '-' + mapping['color-color'][model[-2:]] + '-' + view + '.jpg'
            photo['models'][model][view] = {'old_path': photo_path, 'name': new_name}
            
            with Image.open(photo_path) as image:
                image = image.resize((mapping['view-sizes'][view][0], mapping['view-sizes'][view][1]))
                image.save('./Data/CleanPhotos/Models/' + model + '/' + new_name)
    # print(photo)


if __name__ == '__main__':
    main()
