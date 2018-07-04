def replace(line):
    array = line

f = open("in.txt",'r')
outFile = open("out.txt","a")

for line in f:
    line = line.replace("object-oriented","JavaJavaJava")
    outFile.write(line)

outFile.close()
f.close()