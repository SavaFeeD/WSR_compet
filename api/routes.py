from flask import request, jsonify
import pandas as pd
import tabula
import preprocessing


def route(app):
    @app.route('/', methods=['GET'])
    def home():
        return '''<h1>Апи!</h1>'''

    @app.route('/api/recommendation', methods=['POST'])
    def recommendation():
        try:
            pdf = request.files['pdf']
            df = tabula.read_pdf(pdf, pages='all')[0]
            print()
            if df.columns[0] != 'Ключевые навыки' or df.columns[1] != 'Процент освоения':
                raise TypeError
        except:
            return jsonify({
                "status": False,
                "body": {
                    "message": 'Файл не пришел или файл не pdf формата'
                }
            })

        df = df.rename(columns={'Ключевые навыки': 'skills', 'Процент освоения': 'percent'})

        # ..предобработка формирование файла и отаем путь до файла

        filename = 'Example'
        return jsonify({
            "status": True,
            "data": {
                "url": f"http://127.0.0.1:5000/static/{filename}.pdf",
            }
        })
