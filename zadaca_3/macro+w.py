import re

class Macro:
    def __init__(self):
        self._flag = False
        self._line = ""
        self._errm = ""
        self._while_label_counter = 0
        self.lines = []
        
    def _parse_macros(self):
        self._iter_lines(self._parse_macro)
    
    def _get_next_line(self):
        if not self.lines:
            return None
        return self.lines.pop(0)
    
    def _parse_macro(self, line, p, o):
        if line[0]!="$":
            return line
        else:
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
            elif line[1:] == 'WHILE':
                A = re.split("[(,)]", line)[1]
                local_while_label = "WHILE_START_" + str(self._while_label_counter)
                local_while_end_label = "WHILE_END_" + str(self._while_label_counter)
                self._while_label_counter += 1

                lines.append("(" + local_while_label + ")")
                lines.append("@" + A)
                lines.append("D=M") 
                lines.append("@" + local_while_end_label)
                lines.append("D;JEQ") 

                while True:
                    next_line = self._get_next_line()
                    if not next_line or next_line.strip() == "$END":
                        break
                    parsed_line = self._parse_macro(next_line)
                    lines.extend(parsed_line)
                
                lines.append("@" + local_while_label)
                lines.append("0;JMP")  
                lines.append("(" + local_while_end_label + ")")  
            else:
                self._flag = False
                self._line = o
                self._errm = "Invalid Macro!" 
        return lines   