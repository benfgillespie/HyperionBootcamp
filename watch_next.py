import spacy

# read in information from movies.txt assuming utf 8
with open('movies.txt', 'r', encoding='utf-8') as f:
    movies = f.readlines()
    # strip weird characters out of the list
    movies = [x.strip() for x in movies]
    # remove backslashes
    movies = [x.replace('\\', '') for x in movies]

# separate the movies into a list of lists
movies = [x.split(':') for x in movies]


planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(movies)


# load advanced language model
nlp = spacy.load('en_core_web_md')

# create a spacy object for planet hulk
planet_hulk = nlp(planet_hulk)

# create a list of tuples with the movie name and the similarity score
movie_scores = []

# iterate over movie list, and compare each movie to planet hulk
for movie in movies:
    # create a spacy object for each movie description
    movie_desc = nlp(movie[1])
    # add the score to a list of scores
    movie_scores.append((movie[0], planet_hulk.similarity(movie_desc)))

print(movie_scores)
print("The movie with the highest similarity score is: ", max(movie_scores, key=lambda x: x[1]))
