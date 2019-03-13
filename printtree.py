def treePrint(tree, level=0):
  if isinstance(tree, dict):  
    for k,v in tree.items():
      print("|  "*level + "├── ", end="")
      print(k)
      treePrint(v, level+1)
  elif isinstance(tree, list):
      for x in tree:
          treePrint(x, level)
  else:
      print("|  "*level + "├── ", end="")
      print(tree)

def treePrint2(tree, level=0, prevLevel=[], isLastItem=False):
  def getPrefix(level, prevLevel=[], isLastItem=False):
      while len(prevLevel) < level+1:
        prevLevel.append(False)
      prevLevel[level] = isLastItem
      prefix = ""
      for i in range(level):
        if prevLevel[i]:
          prefix = prefix + "   "
        else:
          prefix = prefix + "|  "
      if isLastItem:
        prefix += "└── "
      else:
        prefix += "├── "
      return prefix

  if isinstance(tree, dict):
    i = 0
    len_ = len(tree)
    #print(f"len:{len_}")
    for k,v in tree.items():
      i += 1
      prefix = getPrefix(level, prevLevel, i==len_)
      print(f"{prefix}{k}")
      if not isinstance(v, list) and not not isinstance(v, dict):
        isLastItem = True
      treePrint2(v, level+1, prevLevel, isLastItem)
  elif isinstance(tree, list):
      i = 0
      len_ = len(tree)
      for x in tree:
          i += 1
          treePrint2(x, level, prevLevel, i==len_)
  else:
      prefix = getPrefix(level, prevLevel,isLastItem)
      print(f"{prefix}{tree}")

if __name__ == "__main__":
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
    #treePrint(tree)
    treePrint2(tree)
