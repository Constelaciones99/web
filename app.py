#APP.PY

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from utils import find_similar_images

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'image_api/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Ruta para cargar la imagen y compararla con las del directorio 'productos'
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file part"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Guardar la imagen cargada en la carpeta 'uploads'
    upload_path = os.path.join('image_api', 'uploads', file.filename)
    file.save(upload_path)

    # Ruta donde se encuentran las imágenes a comparar (en 'productos')
    image_dir = os.path.join('..', 'storage', 'app', 'public', 'productos')

    # Llamar a la función que encuentra las imágenes similares
    similar_images = find_similar_images(upload_path, image_dir)

    # Retornar los resultados en formato JSON
    return jsonify(similar_images)

if __name__ == '__main__':
    app.run(debug=True)
