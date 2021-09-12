from peewee import *
from datetime import datetime

database = MySQLDatabase('app_db', host='127.0.0.1', user='root', password='mi_clave_root', port=6033)


class User(Model):
    class Meta:
        database = database
        table_name = 'users'

    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    apellido = CharField(max_length=50, unique=True)


    def __str__(self):
        return self.username


class Movie(Model):
    class Meta:
        database = database
        table_name = 'movies'

    title = CharField(max_length=50, unique=True)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


class UserReview(Model):
    class Meta:
        database = database
        table_name = 'user_reviews'

    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user.username} puntuó {self.score} a {self.movie.title}"

database.connect()

database.create_tables([
    User,
    Movie,
    UserReview
])
