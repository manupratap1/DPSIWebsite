#Use this file so that changes are reflected in all files
import os
directory = os.getcwd()
with open(directory + "/" + "header_new.html") as f:
    to_replace = f.read()
start_point = '<div class="nav">'
end_point = '<!--top header inserted here-->'
for filename in os.listdir(directory):
    if filename.endswith("html") and (filename != "header_new.html"):
        with open(directory + "/" + filename, "r") as f:
            txt = f.read()
        idx_beg = txt.find(start_point)
        idx_end = txt.find(end_point)
        txt = txt[:idx_beg] + to_replace + txt[idx_end:]

        if txt.find('<link rel="stylesheet" type="text/css" href="css/style.css">') == -1:
            idx_beg = txt.find("<head>")
            txt = txt[:idx_beg+6] + '\n<link rel="stylesheet" type="text/css" href="css/style.css">' + txt[idx_beg+6:]

        if txt.find('<script src="nav_script.js"></script>') == -1:
            idx_beg = txt.find("<head>")
            txt = txt[:idx_beg+6] + '\n<script src="nav_script.js"></script>' + txt[idx_beg+6:]

        if txt.find('<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>') == -1:
            idx_beg = txt.find("<head>")
            txt = txt[:idx_beg+6] + '\n<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>' + txt[idx_beg+6:]
    

        txt = txt.replace('<script src="js/jquery.min.js"></script>', " ")
        txt = txt.replace('<script type="text/javascript" src="./gallerycode/jquery-1.11.1.min.js"></script>', " ")
        txt = txt.replace('.active {\nbackground-color: white;\n}', ' ')

        with open(directory + "/" + filename, "w") as f:
            f.write(txt)

