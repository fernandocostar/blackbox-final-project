import os

imgs_names = []

for files in os.walk("images", topdown=False):
    for j in range(len(files[2])):
        imgs_names.append(files[2][j].replace(".png", ""))
print(imgs_names[:2000])
