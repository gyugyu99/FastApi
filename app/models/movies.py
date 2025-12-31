from typing import Any, List, Optional


class MovieModel:
    _data: List["MovieModel"] = []
    _id_counter: int = 1

    def __init__(self, title: str, director: str, year: int) -> None:
        self.id = MovieModel._id_counter
        self.title = title
        self.director = director
        self.year = year

        MovieModel._data.append(self)
        MovieModel._id_counter += 1

    @classmethod
    def create(cls, title: str, director: str, year: int) -> "MovieModel":
        """새로운 영화 추가"""
        return cls(title, director, year)

    @classmethod
    def get(cls, **kwargs: Any) -> Optional["MovieModel"]:
        """단일 객체를 반환 (없으면 None)"""
        for movie in cls._data:
            if all(getattr(movie, key) == value for key, value in kwargs.items()):
                return movie
        return None

    @classmethod
    def filter(cls, **kwargs: Any) -> List["MovieModel"]:
        """조건에 맞는 객체 리스트 반환"""
        return [movie for movie in cls._data if all(getattr(movie, key) == value for key, value in kwargs.items())]

    def update(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                if value is not None:
                    setattr(self, key, value)

    def delete(self) -> None:
        """현재 인스턴스를 _data 리스트에서 삭제"""
        if self in MovieModel._data:
            MovieModel._data.remove(self)

    @classmethod
    def all(cls) -> List["MovieModel"]:
        """모든 영화 반환"""
        return cls._data

    def __repr__(self) -> str:
        return f"MovieModel(id={self.id}, title='{self.title}', director='{self.director}', year={self.year})"
