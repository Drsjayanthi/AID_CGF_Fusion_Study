
import random
import numpy as np
import torch
from torch.utils.data import Dataset
from PIL import Image

class AIDDataset(Dataset):
    def __init__(self, df, transform=None):
        self.paths = df["path"].tolist(); self.labels = df["label"].astype(int).tolist(); self.transform = transform
    def __len__(self): return len(self.paths)
    def __getitem__(self, i):
        img = Image.open(self.paths[i]).convert("RGB")
        if self.transform: img = self.transform(img)
        return img, self.labels[i]

class RandomRightAngleRotation:
    # Aerial scenes have no canonical up: rotate by a random multiple of 90 degrees.
    def __call__(self, img):
        k = random.choice([0, 90, 180, 270])
        return img.rotate(k) if k else img

def seed_worker(worker_id):
    s = torch.initial_seed() % 2**32
    np.random.seed(s); random.seed(s)
