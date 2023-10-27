from typing import Optional

class Properties:
    
    
    def __init__(self, source : str):
        self.aMap = {}
        comment = "#"
        with open(source) as file:
            for line in file.readlines():
                strippedLine = line.strip()
                if line.startswith(comment):
                    continue
                splitLine = strippedLine.split("=")
                key = splitLine[0].strip()
                value = splitLine[1].strip()
                self.aMap[key] = value
                
    def getValue(self, key : str) -> Optional[str]:
        return self.aMap[key]
    
    def setValue(self, key : str, value : str):
        self.aMap[key] = value