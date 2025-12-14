from ultralytics import YOLO
import os

# Load YOLO model once
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pt")
model = YOLO(MODEL_PATH)

CONFIDENCE_THRESHOLD = 0.4


def detect_vegetables(image_path):
    """
    Detect vegetables from an image path using YOLO.

    Args:
        image_path (str): path to image file

    Returns:
        list: detected vegetable names
    """

    if not image_path or not os.path.exists(image_path):
        return []

    try:
        results = model(image_path, verbose=False)[0]
    except Exception as e:
        print("YOLO error:", e)
        return []

    detected = set()

    if not results.boxes:
        return []

    for box in results.boxes:
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])

        if conf < CONFIDENCE_THRESHOLD:
            continue

        label = results.names.get(cls_id, "").lower().strip()
        label = label.replace("_", " ")

        if label:
            detected.add(label)

    return sorted(list(detected))
