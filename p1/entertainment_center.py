import media
import fresh_tomatoes

interstellar = media.Movie("Interstellar","Mankind was born on Earth. It was never meant to die here.",
	'http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB',
	'https://www.youtube.com/watch?v=0vxOhd4qlnA')

dark_knight = media.Movie("The Dark Knight","The night is darkest before the dawn.",
	"http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
	"https://www.youtube.com/watch?v=yQ5U8suTUw0")
	
dark_knight_rises = media.Movie("The Dark Knight Rises", "A Fire Will Rise",
                                "http://upload.wikimedia.org/wikipedia/en/thumb/8/83/Dark_knight_rises_poster.jpg/220px-Dark_knight_rises_poster.jpg",
                                "https://www.youtube.com/watch?v=g8evyE9TuYk")	
	


#print interstellar.title
#print interstellar.storyline
#interstellar.show_trailer()
#interstellar.show_poster()

movies = [interstellar,dark_knight,dark_knight_rises]

fresh_tomatoes.open_movies_page(movies)

