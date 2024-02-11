from typing import List


class PrepMovies:
    def __init__(self, movies: List[str]):
        self.movies = movies
        self.root_dir = "P:/Movies/"


from pathlib import Path
print(Path(__file__).parents[2])