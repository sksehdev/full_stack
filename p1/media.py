import webbrowser

class Movie():
	"""
	Description : Class for the movie

	Movie constructor takes four parameters :
	title : Title for the movie
	storyline : Tagline for the movie
	poster_image_url: Poster URL for the movie
	trailer_youtube_url : Youtube URL for the movie 

	Usage :

	interstellar = media.Movie("Interstellar","Mankind was born on Earth. 
		It was never meant to die here.",
	'http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB',
	'https://www.youtube.com/watch?v=0vxOhd4qlnA')

        """

	def __init__(self, title,storyline,poster_image,trailer_youtube):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)

	def show_poster(self):
		webbrowser.open(self.poster_image)






