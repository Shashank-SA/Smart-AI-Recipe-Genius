from PIL import Image
import os
import uuid

def load_image(image_path):
    """
    Backward compatibility function.
    Loads image safely from disk.
    """
    try:
        return Image.open(image_path)
    except Exception:
        return None
def save_uploaded_image(uploaded_file, save_dir="storage"):
    """
    Save uploaded Streamlit image safely to disk.

    Args:
        uploaded_file: Streamlit uploaded file object
        save_dir (str): Directory to save images

    Returns:
        str | None: Path to saved image
    """

    if uploaded_file is None:
        return None

    os.makedirs(save_dir, exist_ok=True)

    try:
        image = Image.open(uploaded_file).convert("RGB")
    except Exception as e:
        print("Image loading error:", e)
        return None

    filename = f"{uuid.uuid4().hex}.jpg"
    image_path = os.path.join(save_dir, filename)

    try:
        image.save(image_path, format="JPEG", quality=95)
    except Exception as e:
        print("Image saving error:", e)
        return None

    return image_path


def resize_image(image_path, max_size=(640, 640)):
    """
    Resize image while maintaining aspect ratio.

    Args:
        image_path (str)
        max_size (tuple)

    Returns:
        str: Same image path after resize
    """

    if not os.path.exists(image_path):
        return image_path

    try:
        img = Image.open(image_path)
        img.thumbnail(max_size)
        img.save(image_path)
    except Exception as e:
        print("Image resize error:", e)

    return image_path


def validate_image(image_path):
    """
    Validate image before sending to YOLO.

    Returns:
        bool
    """
    if not image_path or not os.path.exists(image_path):
        return False

    try:
        Image.open(image_path)
        return True
    except Exception:
        return False
