import re

def _parse_macros(self):
    
    self._iter_lines(self._parse_macro)
    
def _parse_macro(self, line, p, o):
    if line[0]!="$":
        return line
    else:
        lines=[]
        if line[1]=='M' and line[2]=='V':
            A = re.split("[(,)]", line)[1]
            B = re.split("[(,)]", line)[2]
            lines.append("@" + A)
            lines.append("D=M")
            lines.append("@" + B)
            lines.append("M=D")
        elif line[1]=='S'and line[2]=="W"and line[3]=='P':
            A = re.split("[(,)]", line)[1]
            B = re.split("[(,)]", line)[2]
            lines.append("@" + A)
            lines.append("D=M")
            lines.append("@SwapValue")
            lines.append("M=D")
            lines.append("@" + B)
            lines.append("D=M")
            lines.append("@" + A)
            lines.append("M=D")
            lines.append("@SwapValue")
            lines.append("D=M")
            lines.append("@" + B)
            lines.append("M=D")
        elif line[1]=='S' and line[2]=='U' and line[3]=='M':
            A = re.split("[(,)]", line)[1]
            B = re.split("[(,)]", line)[2]
            D = re.split("[(,)]", line)[3]
            lines.append("@" + A)
            lines.append("D=M")
            lines.append("@" + B)
            lines.append("D=D+M")
            lines.append("@" + D)
            lines.append("M=D")
        else:
            self._flag = False
            self._line = o
            self._errm = "Invalid Macro!" 
    return lines   