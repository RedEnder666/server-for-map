from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def map_page():
    map_data = [
            {
            'ind': 0,
            'latitude': 55.639141,
            'longitude': 34.878836,
            'hint': 'Природный парк Гагаринский',
            'balloon': 'Описание',
            'icon_path': 'static/icon.png',
            'question': 'Какое событие привело к возникновению Братской могилы в поселке Карманово?',
            'options': [
                'Завершение строительства местного моста',
                'Освобождение мест в августе – сентябре 1942 года',
                'Открытие местного музея истории'],
            'rightind': 1,
        },
        {
            'ind': 1,
            'latitude': 54.785733,
            'longitude': 31.879876,
            'hint': 'Музей-заповедник «Гнездово»',
            'balloon': 'Описание',
            'icon_path': 'static/icon.png',
            'question': 'Что раскинулось за городищем и древним посадом в комплексе музей-заповедника «Гнездово»?',
            'options': [
                'Огромный некрополь из более чем трех тысяч курганов',
                'Множество художественных статуй и фонтанов',
                'Современный парк аттракционов'],
            'rightind': 0,
        },
        {
            'ind': 2,
            'latitude': 54.78825000,
            'longitude': 32.05420000,
            'hint': 'Свято-успенский собор',
            'balloon': 'Описание',
            'icon_path': 'static/icon.png',
            'question': 'Сколько лет длилось возведение Свято-Успенского собора на месте прежнего соборного храма?',
            'options': [
                'Двадцать лет (с 1900 г.)',
                'Пятьдесят лет (с 1750 г.)',
                'Около ста лет (с 1676 г.)', ],
            'rightind': 2,
        },
        {
            'ind': 3,
            'latitude': 54.78444,
            'longitude': 32.05139,
            'hint': 'Смоленская крепость',
            'balloon': 'Описание',
            'icon_path': 'static/icon.png',
            'question': 'Сколько башен изначально включала стена Смоленской крепости, и сколько из них сохранилось по сей день?',
            'options': [
                '20 башен изначально, все сохранились',
                '38 башен изначально, 17 сохранилось',
                '50 башен изначально, 10 сохранилось',
                'Все башни сохранились'],
            'rightind': 1,
        },
        {
            'ind': 4,
            'latitude': 54.788160,
            'longitude': 32.053920,
            'hint': 'Смоленский государственный университет(СмолГУ)',
            'balloon': 'Описание',
            'icon_path': 'static/icon.png',
            'question': 'В каком году был образован Смоленский государственный университет?',
            'options': [
                '1930 г.',
                '1918 г.',
                '1998 г.'],
            'rightind': 1,
        },
        {
            'ind': 5,
            'latitude': 54.796443,
            'longitude': 32.037759,
            'hint': 'Церковь Петра и Павла',
            'balloon': 'Описание',
            'icon_path': 'static/icon.png',
            'question': 'В каком году церковь Петра и Павла была реставрирована по проекту П.Д. Барановского?',
            'options': [
                '1980 г.',
                '2000 г.',
                '1967 г.'],
            'rightind': 2,
        },
    ]

    return render_template('index.html', map_data=map_data)

@app.route('/get_map_data', methods=['GET'])
def get_map_data():
    map_data = [
    ]

    return jsonify(map_data)

@app.route('/handle_click', methods=['POST'])
def handle_click():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')

    response_data = {'nearest_point': {'latitude': ..., 'longitude': ...}}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

