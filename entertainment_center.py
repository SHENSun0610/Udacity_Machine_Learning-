"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    beauty_and_the_beast = media.Movie("Beauty and the Beast",
                          "An adaptation of the fairy tale about a monstrous-looking prince and a young woman who fall in love",
                          "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                          "https://www.youtube.com/watch?v=OvW_L8sTu5E",
                          "Novermber,14,2016")

    toy_story = media.Movie("Toy story",
                          "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room",
                          "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                          "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                          "May, 29, 2009")

    res_evil = media.Movie("Resident Evil",
                           "Zombie-causing virus escapes from the lab",
                           "https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",
                           "https://www.youtube.com/watch?v=u6uDnd_v5Bw",
                           "March 15, 2002")
    furious = media.Movie("Furious Seven", 
                          "Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother",
                          "https://upload.wikimedia.org/wikipedia/sco/b/b8/Furious_7_poster.jpg",
                          "https://www.youtube.com/watch?v=Skpu5HaVkOc",
                          "Novermber 1, 2014")

    avatar = media.Movie("Avatar",
                         "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home",
                         "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                         "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                         "Novermber, 9, 2009")

    the_dish = media.Movie("The Dish",
                           "A film about a radio telescope",
                           "https://upload.wikimedia.org/wikipedia/en/4/4a/Thedish_poster.jpg",
                           "https://www.youtube.com/watch?v=2TAqXENo1rA",
                           "October 19, 2000")


    # Store the Movie objects in a list.
    movies = [beauty_and_the_beast, toy_story, res_evil, furious, avatar, the_dish]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
