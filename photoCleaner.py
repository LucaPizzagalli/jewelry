from glob import glob
from pathlib import Path
from PIL import Image

mapping = {
    'number-view': {
        '1': 'box',
        '2': 'oblique',
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
    },
    'color-color': {
        'OG': 'yellow-gold'
    }
}


def main():
    photo = {'models': {}}
    model_paths = glob('../RawPhotos/Models/*/')
    for model_path in model_paths:
        model = model_path.split('/')[-2]
        photo['models'][model] = {}
        photo_paths = glob(model_path + '*')
        Path('../CleanPhotos/Models/' + model).mkdir(parents=True, exist_ok=True)

        for photo_path in photo_paths:
            name = photo_path.split('/')[-1].split('.')[0]
            if name not in mapping['number-view'].keys():
                raise Exception('LUCAERROR: nome sconosciuto: ' + photo_path)
            view = mapping['number-view'][name]
            new_name = name + '-silver-ring-' + model[2:5] + '-' + mapping['color-color'][model[-2:]] + '-' + view + '.jpg'
            photo['models'][model][view] = {'old_path': photo_path, 'name': new_name}
            
            with Image.open(photo_path) as image:
                image = image.resize((mapping['view-sizes'][view][0], mapping['view-sizes'][view][1]))
                image.save('../CleanPhotos/Models/' + model + '/' + new_name)
    print(photo)


if __name__ == '__main__':
    main()
