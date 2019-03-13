# Print a tree like list


For example, you have a tree like dictionary:
```
tree = {
    "level0_1":{
        "level1_1":[
        "level2_1",
        "level2_2"
        ],
        "level1_2":{
        "level2_3": {
            "level3_1": "Cool",
            "level3_2": "yeah"
        },
        
        "level2_4": "end"
        }
    },
    "level0_2": {
        "level1_3": "level2_5",
        "level1_4": [
        "level2_8",
        "level2_9"
        ]
    }
}
```

Run this program, it will print like:
```
$ python printtree.py
├── level0_1
|  ├── level1_1
|  |  ├── level2_1
|  |  └── level2_2
|  └── level1_2
|     ├── level2_3
|     |  ├── level3_1
|     |  |  └── Cool
|     |  └── level3_2
|     |     └── yeah
|     └── level2_4
|        └── end
└── level0_2
   ├── level1_3
   |  └── level2_5
   └── level1_4
      ├── level2_8
      └── level2_9
```