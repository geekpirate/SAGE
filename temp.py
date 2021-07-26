import docx2txt

# read in word file
delim = "__________________________________________________________________________"
t = []
temp = []
out = []
ar = []

result = docx2txt.process("/Users/abhinavreddy/Downloads/1_10-1_16 COVID-19 Long-Haulers Discussion Group copy.docx")
f = open("demofile3.txt", "w")
f.write(result)
f.close()

with open("demofile3.txt") as fp:
    for line in fp:
        if line == "Like\n" or line == "Comment\n" or line == "Write a comment…\n":
            continue
        if line.endswith("Comments\n") or line.endswith("Comment\n"):
            t.append(("".join("Break\n")))
            continue
        if not line.isspace():
            t.append(("".join(line)))
fd = open("demofile.txt", "w")
fd.writelines(t)
fd.close()
with open("demofile.txt") as fd:
    Lines = fd.read()
    ar = Lines.split(delim)

for i in ar:
    temp.append(i.split("\n"))
fr = open("post.txt", "w")
for p in temp:
    #print(p.count("Break"))
    if p.__contains__(" · "):
        for i in range(p.index(" · ")+1, p.index("Break")):
            if p[i].isnumeric():
                continue
            out.append(p[i])
        out.append("\n" + delim + "\n")

fr.writelines(out)
fr.close()
