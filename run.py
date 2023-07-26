import json
import time
import random

import numpy as np
import pydantic
from config import RESULTS_DIR
from qdrant_client import QdrantClient
from qdrant_client.http import models


np.random.seed(1)
random.seed(1)

COLLECTION_NAME = "bench"


def bench(vector_num: int, dim: int, collection_name: str = COLLECTION_NAME, **_) -> float:
    print(f"Launched bench with vector num = {vector_num}, dim = {dim}")
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=dim, distance=models.Distance.COSINE),
    )

    start = time.perf_counter()
    vectors = np.random.random((vector_num, dim))
    client.upload_collection(
        COLLECTION_NAME,
        vectors=vectors,
    )
    elapsed = time.perf_counter() - start
    print(f"Elapsed time: {elapsed}")
    client.delete_collection(collection_name)
    return elapsed


if __name__ == "__main__":
    client = QdrantClient()
    grid = [
        {"dim": 1536, "vector_num": 10_000, "display_name": "10k 1536-d"},
        {"dim": 768, "vector_num": 50_000, "display_name": "50k 768-d"},
        {"dim": 384, "vector_num": 100_000, "display_name": "100k 384-d"},
    ]
    with open(RESULTS_DIR / "bench.jsonl", "a") as f:
        for params in grid:
            f.write(
                json.dumps(
                    {"elapsed": bench(**params), "version": pydantic.VERSION, **params}
                )
                + "\n"
            )
