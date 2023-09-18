#!/usr/bin/env python
# coding: utf-8

# In[6]:


class LightNovel:
    def __init__(self, novel_id, title, author, is_available=True):
        self.novel_id = novel_id
        self.title = title
        self.author = author
        self.is_available = is_available
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Novel ID: {self.novel_id}")
        print(f"Author: {self.author}")
        availability = "Available" if self.is_available else "Not Available"
        print(f"Availability: {availability}")

        
class RentalSystem:
    def __init__(self):
        self.novels = []
        
    def add_novel(self, novel):
        self.novels.append(novel)
        print(f"Light Novel {novel.novel_id} added to the system")
        
    def remove_novel(self, novel_id):
        for novel in self.novels:
            if novel.novel_id == novel_id: 
                self.novels.remove(novel)
                print(f"Novel with {novel_id} removed from system")
                return
        print(f"Novel with {novel_id} is not in system")
        
    def display_available_novels(self):
        available_novels = [novel for novel in self.novels if novel.is_available]
        if not available_novels:
            print("No light novels available.")
        else:
            print("Available Light Novels:")
            for novel in available_novels:
                novel.display_info()
                
    def rent_novel(self, novel_id):
        for novel in self.novels:
            if novel.novel_id == novel_id:
                if novel.is_available:
                    novel.is_available = False
                    print(f"Light Novel rented with ID {novel_id}")
                else:
                    print(f"Light Novel with ID {novel_id} is not available")
                return
        print(f"Light Novel with ID {novel_id} is not in the library")
        
        
novel_rental_system = RentalSystem()

novel_1 = LightNovel("LN01", "Are you okay with having slightly older girlfriend", "Novel Writer_01")
novel_2 = LightNovel("LN02", "Our Classmate Does not know what are we doing in their room", "Novel Writer_02")
novel_3 = LightNovel("LN03", "My Days with Step-sister", "Novel Writer_03")
novel_4 = LightNovel("LN04", "Angel Next Door Spoils me Rotten", "Novel Writer_04")
novel_5 = LightNovel("LN05", "My Stepmom Daughter is My Ex", "Novel Writer_05")

novel_rental_system.add_novel(novel_1)
novel_rental_system.add_novel(novel_2)
novel_rental_system.add_novel(novel_3)
novel_rental_system.add_novel(novel_4)
novel_rental_system.add_novel(novel_5)
print()

novel_rental_system.display_available_novels()
print()

novel_rental_system.rent_novel("LN02")
novel_rental_system.display_available_novels()
print()

novel_rental_system.remove_novel("LN03")
novel_rental_system.display_available_novels()






# In[ ]:




