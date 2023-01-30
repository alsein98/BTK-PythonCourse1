# object speciai methods

class Movie:
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie Created")
        
    def __str__(self):
        return "This is a amovie"
    def __len__(self):
        return self.duration
    def __del__(self):
        print("Movie deleted")
        
m1=Movie("title", "director", 160)
print(m1)
print("--------------------")
print(len(m1))
print(m1.__str__())
print(m1.__len__())
del m1
#print(m1.director)