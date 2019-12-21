# Given an HTML template, this script generates all the Ebay-pages of the products.

from pathlib import Path


def get_pic(pic_name):
    pic_file = Path('images' + pic_name)
    if pic_file.is_file():
        return 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images' + \
            pic_name
    else:
        print('Missing: ' + pic_name)
        return 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/placeholder.jpg'


def generate_item_list(info_list):
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
                    'suggestedUrl1': 'https://www.ebay.it/usr/i.sella_bottegaorafa',
                    'suggestedUrl2': 'https://www.ebay.it/usr/i.sella_bottegaorafa',
                    'suggestedUrl3': 'https://www.ebay.it/usr/i.sella_bottegaorafa',
                    'suggestedUrl4': 'https://www.ebay.it/usr/i.sella_bottegaorafa',
                    'suggestedUrl5': 'https://www.ebay.it/usr/i.sella_bottegaorafa',
                    'suggestedUrl6': 'https://www.ebay.it/usr/i.sella_bottegaorafa'
                }
                for pic_index, pic in enumerate(group['pics']):
                    pic_name = '/products/silver' + item['name'] + pic + '.jpg'
                    item['productPic' + str(pic_index+1)] = get_pic(pic_name)
                item['modelPic'] = 'https://raw.githubusercontent.com/LucaPizzagalli/jewelry/master/images/model1.jpg'
                item_list.append(item)
    return item_list


def main():
    info_list = [
        {
            'type': 'EarringsPadelli',
            'description': 'Orecchini diametro ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Gancio di sicurezza.',
            'sizes': ['12 mm', '14 mm', '20 mm', '30 mm'],
            'prices': [5000, 5500, 6000, 7000],
            'colors': ['Yellow', 'Pink', 'White', 'Black'],
            'pics': ['Front', 'Side', 'Back', 'Bottom', 'Model1', 'Box']
        },
        {
            'type': 'RingPadelli',
            'description': 'Anelli diametro ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Il gambo dell’anello è aperto così da essere facilmente adattabile a qualsiasi dito.',
            'sizes': ['12 mm', '14 mm', '20 mm', '30 mm'],
            'prices': [5500, 6000, 6500, 7000],
            'colors': ['Yellow', 'Pink', 'White', 'Black'],
            'pics': ['Front', 'Side', 'Back', 'Bottom', 'Model1', 'Box']
        },
        {
            'type': 'EarringsPadelliOvali',
            'description': 'Orecchini di dimensione ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Gancio di sicurezza.',
            'sizes': ['20x7 mm', '30x10 mm', '40x13 mm', '50x15 mm'],
            'prices': [7000, 8000, 9200, 10700],
            'colors': ['Yellow', 'Pink', 'White', 'Black'],
            'pics': ['Front', 'Side', 'Back', 'Bottom', 'Model1', 'Box']
        },
        {
            'type': 'EarringsFiori',
            'description': 'Orecchini diametro ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Gancio di sicurezza.',
            'sizes': ['15 mm', '20 mm', '30 mm'],
            'prices': [8000, 9000, 10000],
            'colors': ['Yellow', 'Pink', 'White', 'Black'],
            'pics': ['Front', 'Side', 'Back', 'Bottom', 'Box', 'Model1', 'Box']
        },
        {
            'type': 'RingFiori',
            'description': 'Anelli diametro ***size*** in lastra d’argento 925 millesimi. Realizzati interamente a mano. Tagliati, sbalzati, spazzolati, sabbiati e rifiniti in base al modello: dorati oro giallo o rosè, rodiati in bianco o bruniti al rutenio. Il gambo dell’anello è aperto così da essere facilmente adattabile a qualsiasi dito.',
            'sizes': ['15 mm', '20 mm', '30 mm'],
            'prices': [8000, 9000, 10000],
            'colors': ['Yellow', 'Pink', 'White', 'Black'],
            'pics': ['Front', 'Side', 'Back', 'Bottom', 'Model1', 'Box']
        }
    ]

    item_list = generate_item_list(info_list)

    with open('pageTemplate.html', 'r') as file:
        template_text = file.readlines()

    for item in item_list:
        page_text = template_text.copy()
        for line_index, line in enumerate(page_text):
            for key in item:
                page_text[line_index] = page_text[line_index].replace('***' + key + '***', item[key])
        with open("pages/" + item['name'] + 'Page.html', 'w') as file:
            for line in page_text:
                file.write(line)


if __name__ == "__main__":
    main()
