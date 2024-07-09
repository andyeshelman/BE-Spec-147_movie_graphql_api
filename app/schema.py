import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Movie as MovieModel
from app import db

class MovieType(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel 
        
class Query(graphene.ObjectType):
    movies = graphene.List(MovieType)
    movie = graphene.Field(MovieType, movie_id=graphene.ID(required=True))
    search_movies = graphene.List(MovieType, title=graphene.String())
    
    def resolve_movies(root, info):
        query = db.select(MovieModel)
        return db.session.scalars(query)

    def resolve_movie(root, info, movie_id):
        movie = db.session.get(MovieModel, movie_id)
        return movie
    
    def resolve_search_movies(root, info, title=None):
        query = db.select(MovieModel)
        if title:
            query = query.where(MovieModel.title.ilike(f"%{title}%"))
        return db.session.scalars(query)

    
class AddNewMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        director = graphene.String(required=True)
        release_year = graphene.Int(required=True)
        genre = graphene.String(required=True)
        rating = graphene.Float(required=False)
        
    Output = MovieType
    
    def mutate(root, into, title, director, release_year, genre, rating=None):
        new_movie = MovieModel(title=title, director=director, release_year=release_year, genre=genre, rating=rating)
        return new_movie


class UpdateMovie(graphene.Mutation):
    class Arguments:
        movie_id = graphene.ID(required=True)
        title = graphene.String()
        director = graphene.String()
        release_year = graphene.Int()
        genre = graphene.String()
        rating = graphene.Float()

    movie = graphene.Field(MovieType)
    
    def mutate(root, into, movie_id, title=None, director=None, release_year=None, genre=None, rating=None):
        movie = db.session.get(MovieModel, movie_id)
        if movie is None:
            return None
        if title:
            movie.title = title
        if director:
            movie.director = director
        if release_year:
            movie.release_year = release_year
        if genre:
            movie.genre = genre
        if rating:
            movie.rating = rating
        db.session.commit()
        return UpdateMovie(movie=movie)


class DeleteMovie(graphene.Mutation):
    class Arguments:
        movie_id = graphene.ID(required=True)
        
    message = graphene.String()

    def mutate(root, info, movie_id):
        movie = db.session.get(MovieModel, movie_id)
        if movie is None:
            return DeleteMovie(message=f'Movie with ID {movie_id} does not exist')
        else:
            db.session.delete(movie)
            db.session.commit()
            return DeleteMovie(message="User has been deleted")


class Mutation(graphene.ObjectType):
    add_new_movie = AddNewMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)