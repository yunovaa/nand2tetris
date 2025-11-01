//finding R[2] = R[0]*R[1]
// a=R[0], b=R[1]
// c = 0
// if b>0:
//    for i in range(b):
//      c=c+a

@R0
D=M
@a   
M=D  //R[0]=a
@R1
D=M
@b
M=D  //R[1]=b
@c
M=0 //c=0

(LOOP)
@b
D=M
@STOP
D;JEQ
@a
D=M
@c
M=D+M
@b
M=M-1
@LOOP
0;JMP

(STOP)
@c
D=M
@R2
M=D

(END)
@END
0;JMP