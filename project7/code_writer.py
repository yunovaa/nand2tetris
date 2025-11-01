class CodeWriter:

  def __init__(self, output_file):
    self.output_file = output_file
    self.file = open(output_file, 'w')
    self.arithmetic_commands = {'add': 'D+M', 'sub':'M-D' ,
                                'neg':'-M', 'eq': 'JNE', 'gt': 'JLE',
                                'lt':'JGE', 'and':'D&M', 'or':'D|M',
                                'not':'!M'}
    self.loop_counter = 0
    self.logical_commands = {'this': 'THIS','that': 'THAT', 'argument': 'ARG', 'local':'LCL'}

  def write_arithmetic(self, command):
    if command in self.arithmetic_commands.keys():
      command_template = self.arithmetic_commands[command]
      self.file.write(f'//{command}\n')
      if command in ['neg', 'not']:
        self.file.write('@SP\nA=M-1\n')
        self.file.write(f'M={command_template}\n')
      else:
        self.file.write('@SP\nAM=M-1\nD=M\nA=A-1\n')
        if command in ['add', 'sub', 'and', 'or']:
          self.file.write(f'M={command_template}\n')
        else:
          self.file.write(f'D=M-D\n')
          self.file.write(f'M=0\n')
          self.file.write(f'@LOGIC_{self.loop_counter}LOOP\n')
          self.file.write(f'D;{command_template}\n')
          self.file.write('@SP\nA=M-1\n')
          self.file.write(f'M=-1\n')
          self.file.write(f'(LOGIC_{self.loop_counter}LOOP)\n')
          self.loop_counter += 1

  def write_push_pop(self, command, segment, index):
    self.file.write(f'//{command} {segment} {index}\n')
    if command == 'C_PUSH':
      self.push_segment(segment, index)
    elif command == 'C_POP':
      self.pop_segment(segment, index)

  def push_segment(self, segment, index):
    if segment in ['static', 'pointer', 'temp', 'constant']:
      if segment == 'constant':
        self.file.write(f'@{index}\nD=A\n')
      elif segment == 'static':
        self.file.write(f'@static{index}\nD=M\n')
      elif segment == 'temp':
        self.file.write(f'@R{5+index}\nD=M\n')
      elif index == 0:
        self.file.write(f'@THIS\nD=M\n')
      elif index == 1:
        self.file.write(f'@THAT\nD=M\n')
      self.file.write('@SP\nM=M+1\nA=M-1\nM=D\n')
    elif segment in ['local', 'argument', 'this', 'that']:
      pattern = '@{index}\nD=A\n' + '@{segment}\n' + 'A=D+M\nD=M\n' + '@SP\nM=M+1\nA=M-1\nM=D\n'
      self.file.write(pattern.format(index=index, segment=self.logical_commands[segment]))

  def pop_segment(self, segment, index):
    if segment in ['static', 'pointer', 'temp']:
      self.file.write(f'@SP\nAM=M-1\nD=M\n')
      if segment == 'static':
        self.file.write(f'@static{index}\n')
      elif segment == 'temp':
        self.file.write(f'@R{5+index}\n')
      elif index == 0:
        self.file.write(f'@THIS\n')
      elif index == 1:
        self.file.write(f'@THAT\n')
      self.file.write('M=D\n')
    elif segment in ['local', 'argument', 'this', 'that']:
      self.file.write(f'@{index}\nD=A\n')
      if segment == 'local':
        self.file.write('@LCL\n')
      elif segment == 'argument':
        self.file.write('@ARG\n')
      elif segment == 'this':
        self.file.write('@THIS\n')
      elif segment == 'that':
        self.file.write('@THAT\n')
      self.file.write('D=D+M\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n')

  def close(self):
    self.file.write('(END)\n@END\n0;JMP\n')
    self.file.close()

'''
command = CodeWriter("output/test.asm")
command.write_arithmetic('and')
command.write_arithmetic('or')
command.write_arithmetic('not')
command.write_arithmetic('neg')
command.write_arithmetic('add')
command.write_arithmetic('sub')
command.write_arithmetic('eq')
command.write_arithmetic('gt')
command.write_arithmetic('lt')
'''


'''
command = CodeWriter("output/test2.asm")
command.write_push_pop('C_POP', 'static', 1)
command.write_push_pop('C_POP', 'static', 4)
command.write_push_pop('C_POP', 'pointer', 1)
command.write_push_pop('C_POP', 'pointer', 1)
command.write_push_pop('C_POP', 'pointer', 0)
command.write_push_pop('C_POP', 'temp', 0)
command.write_push_pop('C_POP', 'temp', 6)

command.write_push_pop('C_POP', 'local', 1)
command.write_push_pop('C_POP', 'local', 6)
command.write_push_pop('C_POP', 'argument', 1)
command.write_push_pop('C_POP', 'argument', 6)
command.write_push_pop('C_POP', 'this', 1)
command.write_push_pop('C_POP', 'this', 6)
command.write_push_pop('C_POP', 'that', 1)
command.write_push_pop('C_POP', 'that', 6)
'''
'''
command = CodeWriter("output/test3.asm")

command.write_push_pop('C_PUSH', 'constant', 1)
command.write_push_pop('C_PUSH', 'constant', 6)
command.write_push_pop('C_PUSH', 'temp', 1)
command.write_push_pop('C_PUSH', 'temp', 6)
command.write_push_pop('C_PUSH', 'static', 1)
command.write_push_pop('C_PUSH', 'static', 6)
command.write_push_pop('C_PUSH', 'local', 1)
command.write_push_pop('C_PUSH', 'local', 6)
command.write_push_pop('C_PUSH', 'pointer', 0)
command.write_push_pop('C_PUSH', 'pointer', 1)
command.write_push_pop('C_PUSH', 'argument', 1)
command.write_push_pop('C_PUSH', 'argument', 6)
command.write_push_pop('C_PUSH', 'this', 1)
command.write_push_pop('C_PUSH', 'this', 6)
command.write_push_pop('C_PUSH', 'that', 1)
command.write_push_pop('C_PUSH', 'that', 6)
'''
