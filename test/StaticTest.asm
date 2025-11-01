//C_PUSH constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
//C_PUSH constant 333
@333
D=A
@SP
M=M+1
A=M-1
M=D
//C_PUSH constant 888
@888
D=A
@SP
M=M+1
A=M-1
M=D
//C_POP static 8
@SP
AM=M-1
D=M
@static8
M=D
//C_POP static 3
@SP
AM=M-1
D=M
@static3
M=D
//C_POP static 1
@SP
AM=M-1
D=M
@static1
M=D
//C_PUSH static 3
@static3
D=M
@SP
M=M+1
A=M-1
M=D
//C_PUSH static 1
@static1
D=M
@SP
M=M+1
A=M-1
M=D
//sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//C_PUSH static 8
@static8
D=M
@SP
M=M+1
A=M-1
M=D
//add
@SP
AM=M-1
D=M
A=A-1
M=D+M
(END)
@END
0;JMP
