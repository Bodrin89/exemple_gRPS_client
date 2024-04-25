from src.dao.film_dao import FilmDAO
from src.schemas.film_schemas import FilmSchemaOut_Pydantic


class FilmServices:
    @staticmethod
    async def create_film(data_film):
        """Метод для создания фильма"""
        film = await FilmDAO.create_film(data_film)
        return await FilmSchemaOut_Pydantic.from_tortoise_orm(film)
