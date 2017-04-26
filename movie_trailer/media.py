import webbrowser

class Movie():
    #This Class provides all movie names which takes title,story line, image url and youtube url  as arguments

    def __init__(self, movie_title, story_line, poster_image_url, trailer_youtube):
        self.title = movie_title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
