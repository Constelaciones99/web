from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from utils import find_similar_images, build_faiss_index

app = Flask(__name__)
CORS(app)

# Define a path for uploading images
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Ruta con imágenes de productos (ajustado a un directorio fijo)
image_dir = os.path.join(os.getcwd(), 'storage', 'app', 'public', 'productos')

# 🚀 Cargar FAISS index al iniciar
print("🧠 Cargando index FAISS...")
faiss_index, filenames_list, feature_vectors = build_faiss_index(image_dir)
print("✅ FAISS cargado con", len(filenames_list), "imágenes")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    upload_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(upload_path)

    results = find_similar_images(upload_path, faiss_index, filenames_list, feature_vectors)
    print("Resultado FAISS:", results)
    return jsonify(results)

# Modificación para la ejecución en producción
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
