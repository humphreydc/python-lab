print("=== FAVORITE MOVIES LIST ===")
movie_store = []

for i in range(1, 4):
    movie = input(f"Enter movie {i}: ")
    movie_store.append(movie)

print(f"Your Movies: {movie_store}\n")

while True:      
    movie_choice = input("Enter a movie title to search: ") 
    if movie_choice in movie_store:
        print("Yes! 'Avatar' is in your favorite movies list. Enjoy the movie!")
        break
    else:
        print("Movie not found! try again.\n")
