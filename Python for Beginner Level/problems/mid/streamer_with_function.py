"""

Name : User Input
Total NO Of Games Played : USer Input 3
Kills in each Game : USer Input 12 4 0
total Kills 16
Total Deaths : USer Input
Avg Kill : 4

"""
def create_streamer():
    streamer = {
        "name": None, # str
        "gp": None, # str
        "kills_per_game": [], # list
        "total_kills": None, #int
        "total_deaths": None, # int
        "avg_kills": None #int
    }

    streamer["name"] = "CarryMinati"
    streamer["gp"] = 3

    for index in range(0,streamer["gp"]):
        kill = int(input(f"Enter the Kill for game {index + 1}"))
        streamer["kills_per_game"].append(kill)

    streamer["total_kills"] = sum(streamer["kills_per_game"]) # sum 
    streamer["avg_kills"] = streamer["total_kills"] // streamer["gp"] 
    streamer["total_deaths"] = 2 

    
    return streamer

def delete_streamer():
    pass

def update_stramer():
    pass
    