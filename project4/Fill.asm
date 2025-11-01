// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

////

(LISTEN)
@8192
D=A
@n
M=D
@KBD
D=M
@FILLSCREEN
D;JNE




(CLEARSCREEN)
@n
D=M
@SCREEN
A=D+A
M=0
@n
D=M
M=M-1
@CLEARSCREEN
D;JGT

@LISTEN
0;JMP



(FILLSCREEN)
@n
D=M
@SCREEN
A=D+A
M=-1
@n
D=M
M=M-1
@FILLSCREEN
D;JGT

@LISTEN
0;JMP

