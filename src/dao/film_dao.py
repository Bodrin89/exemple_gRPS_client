from src.models import FilmModel


class FilmDAO:
    def __init__(self):
        pass

    @staticmethod
    async def create_film(data_film):
        film = await FilmModel.create(**data_film.model_dump(exclude_unset=True))
        return film
