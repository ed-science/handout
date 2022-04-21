def strip_empty_lines(lines):
  output = []
  for line in lines:
    if line or output:
      output.append(line)
  lines = reversed(output)
  output = []
  for line in lines:
    if line or output:
      output.append(line)
  lines = reversed(output)
  return list(lines)
