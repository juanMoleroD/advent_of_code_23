def findPart(lines: []):
    partX: int = -1
    partY: int = -1
    partLen: int = -1
    for linesIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            if char != '.':
                partX = charIndex
                partY = linesIndex
                
