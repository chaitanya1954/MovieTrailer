from movie_trailer import trailer_outlook
from movie_trailer import media

# Creating instance variables for each movie for the class Movie which takes all required arguments accordingly.
avatar = media.Movie("Avatar","A marine invades alien planet",
                     "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQbybd1RAlDQ6bzFiqeMsoe"
                     "7-MpglppFAXsxKcFjovxzf27WXhVpw",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
iron_man = media.Movie("Ironman","A story of Iron man",
                       "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcT9Vvdvr9CprOQvjR2G1AdY"
                       "idKAOBPIrb-jeHmm5DiKFmYSFclejQ",
                       "https://www.youtube.com/watch?v=wKtcmiifycU")
pursuit_of_happiness = media.Movie("Pursuit of Happyness", "A story of common man to become rich from"
                                   "rags and diffcult situations",
                                   "http://3.bp.blogspot.com/-4FytGzBOiWY/UFs3MjjuDeI/AAAAAAAAAQQ/sDGz5"
                                   "DjV4cM/s1600/the-pursuit-of-happyness.jpg",
                                   "https://www.youtube.com/watch?v=89Kq8SDyvfg")

pirates_of_caribbean = media.Movie("Pirates of Caribbean", "A story of pirates",
                                   "http://cdn.movieweb.com/img.news.tops/NEqPFRXbXtBtuy_3_b.jpg",
                                   "https://www.youtube.com/watch?v=a5V5C8mEVzY")
furious7 = media.Movie("Furious7", "A story of 7 friends",
                       "https://blogs-images.forbes.com/markhughes/files/2015/04/Furious-7.jpg",
                       "https://www.youtube.com/watch?v=yISKeT6sDOg")
kingkong = media.Movie("Kong:Skull Island", "A story of Gorilla",
                       "https://i.ytimg.com/vi/Z4N2s9fFEMs/hqdefault.jpg",
                       "https://www.youtube.com/watch?v=AP0-9FBs2Rs")
movies_list = [avatar,iron_man,pursuit_of_happiness,pirates_of_caribbean,furious7,kingkong]
trailer_outlook.open_movies_page(movies_list)
