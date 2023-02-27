from pathlib import Path
from random import randint

dst = Path(__file__).parent / "fakesource"

for i in range(500):
    size = randint(1, 15) * 1024 * 1024
    with open(dst / f"{i}_size_{size}.mp3", "w") as f:
        pass