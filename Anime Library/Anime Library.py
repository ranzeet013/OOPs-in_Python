#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Anime:
    def __init__(self, title, genre, episode):
        self.title = title
        self.genre = genre
        self.episode = episode
        
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Episode: {self.episode}")
        
        
class AnimeLibrary:
    def __init__(self, name):
        self.name = name
        self.animes = []
        
    def add_anime(self, anime):
        self.animes.append(anime)
        
    def remove_anime(self, anime):
        if anime in self.animes:
            self.animes.remove(anime)
        
    def display_library(self):
        print(f"Anime Library: {self.name}")
        print("----------------------------")
        for anime in self.animes:
            anime.display_info()
            print("---------------------------")
    
anime_1 = Anime("Horimiya", "School, Shonen, RomCom, Slice Of Life", 26)
anime_2 = Anime("Oregairu", "School, RomCom, Slice Of Life", 39)
anime_3 = Anime("Insomaniac After School", "School, Slice Of Life, RomCom", 13)

library = AnimeLibrary("My Anime List")

library.add_anime(anime_1)
library.add_anime(anime_2)
library.add_anime(anime_3)

library.display_library()

library.remove_anime(anime_3)

library.display_library()


# In[ ]:




