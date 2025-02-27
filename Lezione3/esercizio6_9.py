#es6_9

fav_places: dict = {
                    "luca":"rome",
                    "maria":"japan",
                    "pit":"singapore"
                    }

for k, v in fav_places.items():

    print(f"{k.capitalize()}'s favourite place is {v.capitalize()}")