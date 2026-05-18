from flask import Flask, render_template, request, jsonify
import os
from files import vse_fajly_iz_papki, sozdat_fajl, udalit_fajl, pereimenovat_fajl, prochitat_fajl, sortirovat_fajly, razmer_fajla
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def domoj():
    fajly = vse_fajly_iz_papki()
    return render_template('index.html', files=fajly)

@app.route('/create_file', methods=['POST'])
def create_file():
    try:
        dannye = request.get_json()
        imya = dannye.get('filename', 'novyj_fajl')
        tekst = dannye.get('content', '')
        
        novoe_imya = sozdat_fajl(imya, tekst)
        
        return jsonify({
            'status': 'success', 
            'message': f'Файл {novoe_imya} создан',
            'filename': novoe_imya
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/delete_file', methods=['POST'])
def delete_file():
    try:
        dannye = request.get_json()
        imya = dannye.get('filename')
        
        if udalit_fajl(imya):
            return jsonify({'status': 'success', 'message': f'Файл {imya} удален'})
        else:
            return jsonify({'status': 'error', 'message': 'Файл не найден'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/rename_file', methods=['POST'])
def rename_file():
    try:
        dannye = request.get_json()
        staroe = dannye.get('old_name')
        novoe = dannye.get('new_name')
        
        rezultat = pereimenovat_fajl(staroe, novoe)
        
        if rezultat:
            return jsonify({'status': 'success', 'message': f'Переименован в {rezultat}', 'new_name': rezultat})
        else:
            return jsonify({'status': 'error', 'message': 'Файл не найден'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/open_file', methods=['POST'])
def open_file():
    try:
        dannye = request.get_json()
        imya = dannye.get('filename')
        
        soderzhimoe = prochitat_fajl(imya)
        
        if soderzhimoe is not None:
            return jsonify({'status': 'success', 'content': soderzhimoe, 'filename': imya})
        else:
            return jsonify({'status': 'error', 'message': 'Файл не найден'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/get_files', methods=['GET'])
def get_files():
    fajly = vse_fajly_iz_papki()
    return jsonify({'files': fajly})

@app.route('/sorted', methods=['POST'])
def sortirovka():
    fajly = vse_fajly_iz_papki()
    fajly = sortirovat_fajly(fajly, obratno=False)
    return jsonify({'status': 'done', 'files': fajly})

@app.route('/back_sort', methods=['POST'])
def sortirovka_obratno():
    fajly = vse_fajly_iz_papki()
    fajly = sortirovat_fajly(fajly, obratno=True)
    return jsonify({'status': 'done', 'files': fajly})
@app.route('/file_size', methods=['POST'])
def file_size():
    try:
        dannye = request.get_json()
        imya = dannye.get('filename')
        return jsonify({'size': razmer_fajla(imya)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)