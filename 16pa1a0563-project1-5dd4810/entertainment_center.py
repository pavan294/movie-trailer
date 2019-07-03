#!/usr/bin/env python
import media
import fresh_tomatoes


def main():
    """ main function for creating the website """

    # create the instances of movies
    aashiqui = media.Movie("ashiqui",
                                "aashiqui",
                                "http://i.ndtvimg.com/mt/movies/2013-04/asshiqui2-dramatic.jpg",  # NOQA
                                "https://www.youtube.com/embed/g4Tp8arzspw")  # NOQA

    aashiqui = media.Movie("aashiqui2",
                                "ashiqui",
                                "https://i.ytimg.com/vi/Vj9rmKuim3M/maxresdefault.jpg",  # NOQA
                                "https://www.youtube.com/embed/KgsYJRnBNeE")  # NOQA

    chennaiexpress = media.Movie("chennai",
                                "chennai",
                                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTncJKHfE5Dkz7ZgEvYfHozAuLuSsSjCN2B8gB9M1Q7YwkCJs3wKg",  # NOQA
                                "https://www.youtube.com/embed/hZGR5Sj1Bfo")  # NOQA
    premam = media.Movie("premem",
                                        "premem",
                                        "https://english.manoramaonline.com/content/dam/mm/en/entertainment/images/2016/May/29/premam-one-year.jpg.image.784.410.jpg",  # NOQA
                                        "https://www.youtube.com/embed/H1-_SBacAKU")  # NOQA
    baahubali = media.Movie("baahubali",
                                "baahubali",
                                "http://www.lovelytelugu.com/wp-content/uploads/2017/01/16298758_1322879227734849_6679850790624761842_n.jpg",  # NOQA
                                "https://www.youtube.com/embed/qD-6d8Wo3do")  # NOQA
    movies = [
        aashiqui, aashiqui2, chennaiexpress,
        premam, baahubali
    ]
    fresh_tomatoes.open_movies_page(movies)
