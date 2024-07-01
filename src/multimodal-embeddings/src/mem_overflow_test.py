from PIL import Image
from IPython.display import Image as IPythonImage
from IPython.display import display
import io
import torch
from transformers import CLIPProcessor, CLIPModel
import numpy as np
import requests
from scipy.spatial.distance import cosine
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
from itertools import batched
from tqdm import tqdm
from sklearn.decomposition import PCA
import sys

from torchvision.utils import make_grid
from torchvision.io import read_image
from torchvision import transforms


from memory_profiler import profile


# Function to get image embedding


def load_transform_images(image_paths):
    # images = [Image.open(image_path) for image_path in image_paths]

    target_size = (240, 240)
    reshape_transform = lambda image_tensor: transforms.Resize(target_size)(
        image_tensor
    ).expand(3, -1, -1)
    images = [reshape_transform(read_image(image)) for image in image_paths]

    return images


@profile
def get_image_embeddings(image_paths):
    # Load the CLIP model
    clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    images = load_transform_images(image_paths)
    inputs = clip_processor(images=images, return_tensors="pt")
    image_embeddings = clip_model.get_image_features(**inputs)
    return image_embeddings


if __name__ == "__main__":
    images = []
    images.extend(
        Path("data/Footwear/Men/Images/images_with_product_ids").glob("*.jpg")
    )
    images.extend(
        Path("data/Footwear/Women/Images/images_with_product_ids").glob("*.jpg")
    )

    batch_size = 100
    total_batches = int(np.ceil(len(images) / batch_size))

    i = 0
    # image_embeddings = []
    for image_fps in batched(images, batch_size):
        i += 1
        # if i < 155:
        #     continue
        print(f"Processing batch {i}/{total_batches}")

        get_image_embeddings(image_fps)
        # print(sys.getsizeof(image_embeddings) / 1e6)
