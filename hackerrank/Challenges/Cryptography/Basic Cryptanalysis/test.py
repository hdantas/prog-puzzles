import json

d = [
    {      
        "word": "interpolator",
        "frequency": [0.2, 0.2, 0.4, 0.4, 0.2]
    },
    {      
        "word": "interpolator",
        "frequency": [0.2, 0.2, 0.4, 0.4, 0.2]
    }
]
json_string = json.dumps(d)

print json_string