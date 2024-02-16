movie_rating = {
    "The Shawshank Redemption":9,
    "The Lord of the Rings":9,
    "Forrest Gump":8,
    "Inception":8,
    "Star Wars":7,
    "Toy Story":7,
    "The Sound of Music":10
}

movie_name = input('what is the moive name?: ')

def recommend_movie(rating, name):
    if name not in rating:
        print('The movie not found')
        for moviename in rating:
            if rating[moviename] >= 8:
                print(f'Recommend another movies: {moviename}')
    elif rating[name] >= 8:
        print(f"Recommend this movies: {name}")
    else:
        print('The movie rating is low')
        for moviename in rating:
            if rating[moviename] >= 8:
                print(f'Recommend another movies: {moviename}')

recommend_movie(movie_rating,movie_name)


