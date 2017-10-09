import os
directory = os.getcwd()
for filename in os.listdir(directory):
    if filename.endswith(".php") or filename.endswith("html"):
        with open(directory + "/" + filename, "r") as f:
            txt = f.read().replace(".php", ".html")
        with open(directory + "/" + filename, "w") as f:
            f.write(txt)
        os.rename(filename, filename.replace(".php", ".html"))

