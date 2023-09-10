"""
Number of Streamer : 4

Name : CarryMinati
Total NO Of Games Played : USer Input 3
Kills in each Game : USer Input 12 4 0
total Kills 16
Total Deaths : USer Input
Avg Kill : 4

Name : RakaZone
Total NO Of Games Played : USer Input 3
Kills in each Game : USer Input 12 4 0
total Kills 16
Total Deaths : USer Input
Avg Kill : 4

Name : Tanmay Bhatt
Total NO Of Games Played : USer Input 3
Kills in each Game : USer Input 12 4 0
total Kills 16
Total Deaths : USer Input
Avg Kill : 4

Name : Gareeb
Total NO Of Games Played : USer Input 3
Kills in each Game : USer Input 12 4 0
total Kills 16
Total Deaths : USer Input
Avg Kill : 4

Output:

CarryMinati Zombie Killer
Tanmay Bhaat I am Noob
Raka Zone Most Consistent
"""


"""
[
    {
       "name": None, # str
    "gp": None, # str
    "kills_per_game": [], # list
    "total_kills": None, #int
    "total_deaths": None, # int
    "avg_kills": None #int
    }  
    ,
    {
      "name": None, # str
    "gp": None, # str
    "kills_per_game": [], # list
    "total_kills": None, #int
    "total_deaths": None, # int
    "avg_kills": None #int   
    },
]
"""

import streamer_with_function as streamer

n_f_streamers = 3
streamers = []


for index in range(0,n_f_streamers):
    streamer = streamer.create_streamer()
    streamers.append(streamer)

print(streamers)

max_kill_name = None
max_kill = 0

max_deaths = -1
max_deaths_name = None

for streamer in streamers:
    if streamer["total_kills"] > max_kill:
        max_kill = streamer["total_kills"]
        max_kill_name = streamer["name"]
    if streamer["total_deaths"] > max_deaths:
        max_deaths = streamer["total_deaths"]
        max_deaths_name = streamer["name"]

print(f"{max_kill_name} ZOmbie Killer")
print(f"{max_deaths_name} I am Noob")