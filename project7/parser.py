class Parser:
  def __init__(self, input_file):
    with open(input_file, 'r') as file:
      self.input_file = file
      self.lines = [line.split('//')[0].strip() for line in file if line.strip() and not line.startswith('//')]
    self.current_line = 0

  def has_more_lines(self):
    return self.current_line < len(self.lines)

  def advance(self):
    if self.has_more_lines():
      self.current_line += 1

  def command_type(self):
    if self.lines[self.current_line].startswith('push'):
      return 'C_PUSH'
    elif self.lines[self.current_line].startswith('pop'):
      return 'C_POP'
    elif self.lines[self.current_line] in ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']:
      return 'C_ARITHMETIC'

  def arg1(self):
    if self.command_type() != 'C_RETURN':
      if self.command_type() == 'C_ARITHMETIC':
        return self.lines[self.current_line]
      else:
        return self.lines[self.current_line].split()[1]

  def arg2(self):
    if self.command_type() in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
      return int(self.lines[self.current_line].split()[-1])

'''
parser = Parser("input/BasicTest.vm")
for line in parser.lines:
  print('line: ', line)
  print('has_more_lines: ', parser.has_more_lines())
  print('command_type: ', parser.command_type())
  print('arg1: ', parser.arg1())
  print('arg2: ', parser.arg2())

  parser.advance()
'''
