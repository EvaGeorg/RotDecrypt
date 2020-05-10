import string
def map_char(x):
  pos = ((string.ascii_lowercase.index(x)+i)%26)
  return string.ascii_lowercase[pos]

for i in range(1,27):
  f = open('decrypt.txt', "r")
  while (1):
    char = f.read(1)

    char = char.lower()
    if not char:
      break
    if (char.isalpha()):
      encrypted = map_char(char)
      open("decrypted"+str(i)+".txt", "a").write(encrypted)
    else:
      open("decrypted"+str(i)+".txt", "a").write(char)


