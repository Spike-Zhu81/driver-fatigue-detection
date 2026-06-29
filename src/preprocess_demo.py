"""
Demo script for image preprocessing.

This script shows a simplified preprocessing flow used in an
image-based fatigue detection project. The original facial images
and videos are not included in this repository for privacy reasons.
"""

import cv2
import numpy as np


def preprocess_image(image_path: str, image_size: tuple[int, int] = (224, 224)) -> np.ndarray:
    """
    Load an image, resize it, and normalize pixel values.

    Args:
        image_path: Path to an input image.
        image_size: Target image size for the deep learning model.

    Returns:
        Preprocessed image array.
    """
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, image_size)
    image = image.astype("float32") / 255.0

    return image


def main() -> None:
    # Example usage:
    # Replace this path with your own sample image if needed.
    sample_path = "sample.jpg"

    try:
        processed_image = preprocess_image(sample_path)
        print("Preprocessing completed.")
        print("Processed image shape:", processed_image.shape)
    except FileNotFoundError as error:
        print(error)
        print("This is only a demo script. No original facial data is included.")


if __name__ == "__main__":
    main()
