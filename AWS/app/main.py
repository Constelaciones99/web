from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from PIL import Image
from io import BytesIO
import requests

app = FastAPI()

# URL base de las imágenes
image_folder_url = "https://stringify.free.nf/public/storage/productos/"

# Función para descargar imagen desde URL
def load_image_from_url(url):
    resp = requests.get(url)
    img_array = np.asarray(bytearray(resp.content), dtype=np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return image

# Función para comparar imágenes
def compare_images(image1, image2):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(image1, None)
    kp2, des2 = orb.detectAndCompute(image2, None)
    if des1 is None or des2 is None:
        return 0
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    return len(matches)

# ⚡ Función para obtener lista de imágenes desde la URL externa
def get_image_list():
    try:
        # Solicitar la lista de imágenes, ignorando la verificación SSL
        response = requests.get("https://stringify.free.nf/listar-imagenes", verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la lista de imágenes: {e}")
        return []

# 📦 Endpoint para cargar y comparar imagen
@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    image_data = await file.read()
    uploaded_image = Image.open(BytesIO(image_data))
    uploaded_image = uploaded_image.convert('RGB')
    uploaded_image = np.array(uploaded_image)
    uploaded_image = cv2.cvtColor(uploaded_image, cv2.COLOR_RGB2BGR)

    best_match = None
    best_score = 0
    other_matches = []

    image_list = get_image_list()

    for filename in image_list:
        url = image_folder_url + filename
        stored_image = load_image_from_url(url)

        if stored_image is None:
            continue

        score = compare_images(uploaded_image, stored_image)

        if score > best_score:
            if best_match:
                other_matches.append({
                    "filename": best_match,
                    "similarity": best_score
                })
            best_match = filename
            best_score = score

    response_data = {
        "best_match": {
            "filename": best_match,
            "similarity": best_score
        },
        "others": other_matches[:4]
    }

    return JSONResponse(content=response_data)

# Ruta principal
@app.get("/")
def root():
    return {"message": "Servidor funcionando correctamente!"}
