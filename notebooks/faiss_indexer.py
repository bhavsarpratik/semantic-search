import pickle
from pathlib import Path

import faiss
import numpy as np
import pandas as pd
pd.set_option('max_colwidth', 100)

class FAISS:
    def __init__(self, dimensions, gpu=False):
        if gpu:
            # requires faiss-gpu
            res = faiss.StandardGpuResources()  # use a single GPU
            index_flat = faiss.IndexFlatIP(dimensions)  # build a flat index
            self.index = faiss.index_cpu_to_gpu(res, 0, index_flat)
        else:
            self.index = faiss.IndexFlatIP(dimensions)
        self.ids = []

    def add(self, text: str, v: list):
        v = v / np.linalg.norm(v)
        self.index.add(v)
        self.ids.append(text)

    def search(self, v: list, k: int = 10, dataframe=False):
        response = []
        v = v / np.linalg.norm(v)
        distance, item_index = self.index.search(v, k)
        for dist, i in zip(distance[0], item_index[0]):
            if i == -1:
                break
            else:
                item = self.ids[i]
                dist = round(dist, 2)  # dist is actually similarity
                response.append((item, dist))
        if dataframe:
            return pd.DataFrame(response, columns=["text", "cosine_sim"])
        return response

    def save(self, path):
        path = Path(path)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)

        faiss.write_index(self.index, str(path / "index.bin"))
        with open(path / "ids.pkl", "wb") as f:
            pickle.dump(self.ids, f)

    def load(self, path):
        self.index = faiss.read_index(path + "/index.bin")
        self.ids = pickle.load(open(path + "/ids.pkl", "rb"))
