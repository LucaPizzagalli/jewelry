'''Given an HTML template, this script generates all the Ebay-pages of the products.'''

from pathlib import Path
import glob


def get_pic(pic_name):
    '''From the name of an image check if it's present in the folder and return its Url or the Url of a placeholder.'''
    pic_file = Path('images' + pic_name)
    if pic_file.is_file():
        return 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images' + pic_name
    print('Missing: ' + pic_name)
    return 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/placeholder.jpg'


def generate_picture_name(item_type, diameter, color, view):
    type_mapping = {'RingPadelli': 'anello-argento-padelli-silver-ring'}
    number_mapping = {
        'oblique': '1',
        'box': '2',
        'front': '4',
        'side': '5',
        'back': '6',
        'under': '7',
        'model1': '3a',
        'model2': '3b',
        'model3': '3c',
        'model4': '3d',
        'model5': '3e',
    }

    return '{number}-bottega-orafa-ISella-{type}-{diameter}-{color}-{view}.jpg'.format(
        number=number_mapping[view],
        type=type_mapping[item_type],
        diameter= ('00' + diameter)[-6:-3],
        color=color,
        view=view
    )

def generate_item_list(info_list):
    '''From a list of the groups it generates a detailed list of the single products.'''
    item_list = []
    for group in info_list:
        for size in group['sizes']:
            for color in group['colors']:
                item = {
                    'name': group['type'] + size[:2] + color,
                    'productDescription': group['description'].replace('***size***', size),
                    'suggestedPic1': 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/suggested1.jpg',
                    'suggestedPic2': 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/suggested2.jpg',
                    'suggestedPic3': 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/suggested3.jpg',
                    'suggestedPic4': 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/suggested4.jpg',
                    'suggestedPic5': 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/suggested5.jpg',
                    'suggestedPic6': 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/suggested6.jpg',
                    'suggestedUrl1': 'https://www.ebay.it/str/bottegaorafaisella',
                    'suggestedUrl2': 'https://www.ebay.it/str/bottegaorafaisella',
                    'suggestedUrl3': 'https://www.ebay.it/str/bottegaorafaisella',
                    'suggestedUrl4': 'https://www.ebay.it/str/bottegaorafaisella',
                    'suggestedUrl5': 'https://www.ebay.it/str/bottegaorafaisella',
                    'suggestedUrl6': 'https://www.ebay.it/str/bottegaorafaisella'
                }
                for pic_index, view in enumerate(group['pics']):
                    pic_name = '/Items/' + generate_picture_name(group['type'], size, color, view)
                    item['productPic' + str(pic_index+1)] = get_pic(pic_name)
                item['modelPic'] = 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/model1.jpg'
                item_list.append(item)
    return item_list


def main():
    '''The main is just the main, bro.'''
    info_list = [
        # {
        #     'type': 'EarringsPadelli',
        #     'description': 'Orecchini diametro ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Gancio di sicurezza.',
        #     'sizes': ['12 mm', '14 mm', '20 mm', '30 mm'],
        #     'prices': [5000, 5500, 6000, 7000],
        #     'colors': ['Yellow', 'Pink', 'White', 'Black'],
        #     'pics': ['Front', 'Side', 'Back', 'Bottom', 'Model1', 'Box']
        # },
        {
            'type': 'RingPadelli',
            # 'description': 'Anelli diametro ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Il gambo dell’anello è aperto così da essere facilmente adattabile a qualsiasi dito.',
            
            'description': 'I Sella Bottega Orafa è lieta di presentare la sua collezione "i Padelli":<br /><br />anelli in argento 925 millesimi, diametro ***size***. Realizzati a mano nella bottega orafa di Lecco; tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Il gambo dell’anello &egrave; aperto così da essere facilmente adattabile a qualsiasi dito.',
            'sizes': ['12 mm', '14 mm', '20 mm', '30 mm'],
            'prices': [5500, 6000, 6500, 7000],
            'colors': ['yellow', 'pink', 'black', 'white'],
            'pics': ['oblique', 'box', 'front', 'side', 'back', 'under', 'model1', 'model2']
        },
        # {
        #     'type': 'EarringsPadelliOvali',
        #     'description': 'Orecchini di dimensione ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Gancio di sicurezza.',
        #     'sizes': ['20x7 mm', '30x10 mm', '40x13 mm', '50x15 mm'],
        #     'prices': [7000, 8000, 9200, 10700],
        #     'colors': ['Yellow', 'Pink', 'White', 'Black'],
        #     'pics': ['Front', 'Side', 'Back', 'Bottom', 'Model1', 'Box']
        # },
        # {
        #     'type': 'EarringsFiori',
        #     'description': 'Orecchini diametro ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Gancio di sicurezza.',
        #     'sizes': ['15 mm', '20 mm', '30 mm'],
        #     'prices': [8000, 9000, 10000],
        #     'colors': ['Yellow', 'Pink', 'White', 'Black'],
        #     'pics': ['Front', 'Side', 'Back', 'Bottom', 'Box', 'Model1', 'Box']
        # },
        # {
        #     'type': 'RingFiori',
        #     'description': 'Anelli diametro ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Il gambo dell’anello è aperto così da essere facilmente adattabile a qualsiasi dito.',
        #     'sizes': ['15 mm', '20 mm', '30 mm'],
        #     'prices': [8000, 9000, 10000],
        #     'colors': ['Yellow', 'Pink', 'White', 'Black'],
        #     'pics': ['Front', 'Side', 'Back', 'Bottom', 'Model1', 'Box']
        # }
    ]


    item_list = generate_item_list(info_list)

    with open('pageTemplate.html', 'r') as file:
        template_text = file.readlines()

    for item in item_list:
        page_text = template_text.copy()
        for line_index, line in enumerate(page_text):
            for key in item:
                page_text[line_index] = page_text[line_index].replace(
                    '***' + key + '***', item[key])
        with open("pages/" + item['name'] + 'Page.html', 'w') as file:
            for line in page_text:
                file.write(line)


if __name__ == "__main__":
    main()
