import hashlib
import os

filenames = ['file.txt', 't.txt']

with open('output.txt', 'w') as outfile:
  for names in filenames:
    with open(names) as infile:
      outfile.write(infile.read())

    outfile.write("\n")


input_file_path= "output.txt"
output_file_path= "output_new.txt"

output_file = open(output_file_path, "w")

completed_lines_hash = set()

for line in open(input_file_path, "r"):

  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)

output_file.close()
os.remove("output.txt")


sortedList = list()

file = "output_new.txt"
with open (file) as fin:
    for line in fin:
        sortedList.append(line.strip())

sortedList.sort()

new_file = "output.txt"
with open(new_file, "w") as fot:
  for line in sortedList:
    if line != "":
      fot.write(line + "\n")

os.remove("output_new.txt")
