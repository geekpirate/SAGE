import docx2txt
import csv
import os

directory = os.fsencode("/Users/abhinavreddy/Documents/Masters/Project/DE/Comments/COVID Survivor Corps_Comments/")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # filename = filename[:filename.index(".")]
    delim = "__________________________________________________________________________\n"
    t = []
    out = []
    rows = []
    #print(filename)
    if filename.__contains__(".txt"):
        with open("/Users/abhinavreddy/Documents/Masters/Project/DE/Comments/COVID Survivor Corps_Comments/"+filename) as fp:
            lines = fp.readlines()
            for i in range(0, len(lines)):
                t.append(lines[i])
                if lines[i] == delim:
                    t.pop()
                    out.append(t)
                    t = []

        for j in range(0, len(out)):
            temp = out[j]
            for k in range(1, len(temp)):
                # print(temp[k])
                rows.append([temp[k]])
        # print(rows)
        filename = filename[:filename.index(".")]
        fname = "/Users/abhinavreddy/Documents/Masters/Project/DE/Comments_csv/COVID Survivor Corps_Comments/"+filename+".csv"

        # writing to csv file
        with open(fname, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)