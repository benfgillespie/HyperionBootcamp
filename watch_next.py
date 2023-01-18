import spacy


# define function to find best match
def find_best_match(movie_desc, movie_list):
    # load the model
    nlp = spacy.load('en_core_web_md')
    # create a spacy object from the movie
    movie_nlp = nlp(movie_desc)
    # create an empty list to store the similarities
    similarities = []
    # loop through the movies
    for m in movies:
        # create a spacy object from the movie
        m = nlp(m[1])
        # calculate the similarity
        similarity = movie_nlp.similarity(m)
        # append the similarity to the list
        similarities.append(similarity)
    # find the index of the highest similarity
    index = similarities.index(max(similarities))

    # print the name and the score of the best match
    print("The movie with the highest similarity score is ", movies[index][0], "with a score of", max(similarities))


    return movies[index][0]


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

print(find_best_match(planet_hulk, movies))

