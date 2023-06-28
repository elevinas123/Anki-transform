import io
f = io.open("zodziai.txt", mode="r", encoding="utf-8")
y = io.open(".txt", mode="w", encoding="utf-8")
i = 0
j=0
h = []
for x in f:
    if len(x.strip()) == 0 :
        z="gh"
    else:
        x = x.rstrip()
        if (i%3==0):
            j+=1
            h.append("zqe")
        if (j!=0):
            if (h[j-1] !="zqe"):
                g = h[j-1]
                if len(x.strip()) == 0 :
                    g=g + ";" +  "definition nėra"
                else :
                    g=g + ";" +  x
                h[j-1] = g
            else:
                h[j-1] = x
        i+=1
print(len(h))
for x in h:
    y.write(x + "\n")