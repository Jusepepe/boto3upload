views: dict = {
    "front": {
        "pan": ["left","center","right"],
        "tilt": [0, 90, 180]
    },
    "back": {
        "pan": ["left","center","right"],
        "tilt": [0, 90, 180]
    }
}

for view in views:
    print(view)
    for pan in views[view]["pan"]:
        print(pan)
