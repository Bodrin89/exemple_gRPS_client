from tortoise import fields, models


class FilmModel(models.Model):
    class Meta:
        table = 'films'

    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
