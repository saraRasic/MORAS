@R0
D=M;
@s
M=D;
@R2
M=1;
@R1
D=M;
@END
D;JEQ

@j
M=0;
(POW)
	@R0
	D=M;
	@k
	M=D;
	@R1
	D=M;
@j
M=M+1;
D=D-M;
@LOL
D;JEQ

(MULT)
@i
M=0;
(LOOP2_START)
	@k
	D=M;
	@R0
	M=D+M;
@s
D=M;
@i
M=M+1;
D=D-M;
@LOOP2_START
D-1;JGT

@POW
0;JMP


(FIN)
@R0
D=M;
@R2
M=D;

(END)
@END
0;JMP