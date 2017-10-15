#Use this file so that changes are reflected in all files

import os
directory = os.getcwd()
with open(directory + "/" + "header_new.html") as f:
    to_replace = f.read()
start_point = '<div class="nav">'
end_point = '<!--top header inserted here-->'
for filename in os.listdir(directory):
    if filename.endswith("html") and (filename != "header_new.html"):
        idx_beg = txt.find(start_point)
        idx_end = txt.find(end_point)
        txt = txt[:idx_beg] + to_replace + txt[idx_end:]
        if '<link rel="stylesheet" type="text/css" href="css/style.css">' not in txt:
            idx_beg = txt.find("<head>")
            txt = txt[:idx_beg+6] + '\n<link rel="stylesheet" type="text/css" href="css/style.css">' + txt[idx_beg+6:]
        if '<script src="nav_script.js"></script>' not in txt:
            idx_beg = txt.find("<head>")
            txt = txt[:idx_beg+6] + '\n<script src="nav_script.js"></script>' + txt[idx_beg+6:]
        txt = txt.replace('.active {\nbackground-color: white;\n}', '');
        with open(directory + "/" + filename, "w") as f:
            f.write(txt)

