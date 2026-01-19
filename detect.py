from keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Class labels (same order as training)
class_labels = ['pituitary', 'glioma', 'notumor', 'meningioma']

def detect_tumor(model, img_path, image_size=128):
    # Load & preprocess image
    img = load_img(img_path, target_size=(image_size, image_size))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    confidence = float(np.max(predictions))

    label = class_labels[class_index]

    if label == "notumor":
        return "No Tumor", confidence
    else:
        return label.capitalize() + " Tumor", confidence
