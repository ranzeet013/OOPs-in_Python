#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Anime:
    def __init__(self, title, genre, episode, rating):
        self.title = title
        self.genre = genre
        self.episode = episode
        self.rating = rating
        
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Episode: {self.episode}")
        print(f"Rating: {self.rating}")
        
class Anime_Recommendation:
    def __init__(self, name):
        self.name = name
        self.animes = []
        
    def add_anime(self, anime):
        self.animes.append(anime)
        
    def remove_anime(self, anime):
        if anime in self.animes:
            self.animes.remove(anime)
            
    def recommend_anime(self, genre):
        recommend_animes = []
        for anime in self.animes:
            if anime.genre == genre:
                recommend_animes.append(anime)
        return recommend_animes
    
    
anime_1 = Anime("Horimiya", "School", 26, 8)
anime_2 = Anime("Oregairu", "School", 39, 9)
anime_3 = Anime("From Me To You", "Slice of Life, Romcom, School, Shonen", 48, 8)
anime_4 = Anime("One Piece", "Action, Drama, Adventure", 1060, 9.9)

recommendation_system = Anime_Recommendation("Recommend Anime")

recommendation_system.add_anime(anime_1)
recommendation_system.add_anime(anime_2)
recommendation_system.add_anime(anime_3)
recommendation_system.add_anime(anime_4)

recommend_anime = recommendation_system.recommend_anime("School")

print("Recommended Anime in School genre is:")
for anime in recommend_anime:
    anime.display_info()
    print("---------------------------------")


# In[ ]:




