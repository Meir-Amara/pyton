import requests

class Movies:
    def init(self):
        self.__url="https://api.tvmaze.com/shows"
    def get_all_movies(self):
       resp =  requests.get(self.__url)
       data=resp.json()
    #    data=list(map(lambda obj:{obj["name"],obj["rating"]["average"]},data))
       return data