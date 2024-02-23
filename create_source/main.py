with open('output_source/ArduinoAI/main.ino', 'w') as f:
  # Add Header
  with open('create_source/header.txt', 'r') as header:
    f.write(header.read())
  # Add index
  with open('create_source/ArduinoAI/index.html', 'r') as index:
  # Write custom code here
    f.write('\n')
    for line in index.readlines():
      line = line.replace("\\", '\\\\')
      line = line.replace('"', '\\"')
      line = line.replace('\n', '')
      line = f'            client.print("{line}");\n'
      f.writelines([line])
    # f.write(index.readlines())
  # f.write("""
  #           client.print("<p>Hello World!!!</p>");""")
  # Add Footer
  with open('create_source/footer.txt', 'r') as footer:
    f.write(footer.read())
  