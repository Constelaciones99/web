import os
import numpy as np
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf

# Cargar el modelo preentrenado MobileNetV2 para extracción de características
model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, pooling='avg')
image_size = (224, 224)

def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB').resize(image_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return np.expand_dims(img_array, axis=0)

def extract_features(image_path):
    image = preprocess_image(image_path)
    features = model.predict(image)
    return features[0]

def find_similar_images(uploaded_image, image_dir, top_n=5):
    uploaded_features = extract_features(uploaded_image)
    similarities = []

    for filename in os.listdir(image_dir):
        path = os.path.join(image_dir, filename)
        if not os.path.isfile(path): continue
        try:
            features = extract_features(path)
            similarity = cosine_similarity([uploaded_features], [features])[0][0]
            similarities.append((filename, float(similarity)))
        except:
            continue

    similarities.sort(key=lambda x: x[1], reverse=True)
    top_matches = similarities[:top_n]

    response = {
        'best_match': {
            'filename': top_matches[0][0],
            'similarity': round(top_matches[0][1] * 100, 2)
        },
        'others': [
            {'filename': fn, 'similarity': round(score * 100, 2)}
            for fn, score in top_matches[1:]
        ]
    }

    return response
