import sys
from parser import Parser
from code_writer import CodeWriter

class VMtranslator:
  def __init__(self, input_file):
    self.input_file = input_file
    self.output_file = input_file.replace('.vm', '.asm')
    self.code_writer = CodeWriter(self.output_file)
    self.parser = Parser(input_file)

  def translate(self):
    while self.parser.has_more_lines():
      command_type = self.parser.command_type()
      if command_type == 'C_ARITHMETIC':
        self.code_writer.write_arithmetic(self.parser.arg1())
      else:
        self.code_writer.write_push_pop(command_type, self.parser.arg1(), self.parser.arg2())
      self.parser.advance()
    self.code_writer.close()

if __name__ == '__main__':
  pth = sys.argv[1]
  vmtranslator = VMtranslator(pth)
  vmtranslator.translate()