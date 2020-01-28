#! /usr/bin/env python3

f = open('guido_bio.txt')
text = f.read()
f.close()

print(text)

with open('guido_bio.txt') as f_obj:
    bio = f_obj.read()

print(bio)


# ==========
# Handling File Not Found Error
try:
    with open('textfile.txt') as f_obj:
        text = f_obj.read()
except FileNotFoundError:
    text = None

# ==========
# Writing to files
# ==========
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']
with open('oceans.txt', 'w') as fw_obj:
    #fw_obj.writelines(oceans)
    for ocean in oceans:
        print(ocean, file=fw_obj)
        #fw_obj.write(oceans)


with open('oceans.txt', 'a') as fw_obj:
    print("="*25, file=fw_obj)
    print("These are the five oceans in the world",file=fw_obj)

#------- end --------
