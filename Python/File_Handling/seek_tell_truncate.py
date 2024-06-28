with open('file.txt', 'r') as f:
    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(5)
    print(data)
    print(f.tell())

with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())
