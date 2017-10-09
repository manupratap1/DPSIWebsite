#Use this file so that changes are reflected in all files
import os
directory = os.getcwd()
with open(directory + "/" + "header_new.html") as f:
    to_replace = f.read()
start_point = '<div class="nav">'
end_point = '<!--top header inserted here-->'
for filename in os.listdir(directory):
    if (filename.endswith(".php") or filename.endswith("html")) and (filename != "header_new.html"):
        with open(directory + "/" + filename, "r") as f:
            txt = f.read().replace(".php", ".html")
        idx_beg = txt.find(start_point)
        idx_end = txt.find(end_point)
        txt = txt[:idx_beg] + to_replace + txt[idx_end:]
        if '<link rel="stylesheet" type="text/css" href="css/style.css">' not in txt:
            idx_beg = txt.find("<head>")
            txt = txt[:idx_beg+6] + '\n<link rel="stylesheet" type="text/css" href="css/style.css">' + txt[idx_beg+6:]
        with open(directory + "/" + filename, "w") as f:
            f.write(txt)
        idx = 0
        break
        while idx < len(txt):
            idx = txt.find("<style>")


