#!/usr/bin/env python3
import os
# import AbigailSmith as ab, AshrafAbudu as ash, CalebJeffs as cal, ColeFelis as col, DanielWatson as dan, DavidOlson as dav, DeclanCottle as dec, DevinJohnson as dev, DongdiZhao as dong, \
#     ElmerColonMuniz as el, GarrettHarmon as gar, GregorioNunez as gre, KamryByers as kam, KelsieMcKay as kels, LaurynOlson as lauryn, MattThomon as mat, MorganBarlow as mor, NoahSay as noa, \
#     PatrickWong as pat, SpencerBarney as spen, SteveBarton as st

listdir = os.listdir()
class_list = []
# directory = 'C:\Users\Optiplex 9010\OneDrive\Documents\GitHub\INFO-1200-X02-Fall-2022'
directory = "files"
 
# iterate over files in
# that directory

print("The members of the fall 2022 programming I class are:")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if filename == "README.md" or "strat.py":
        break
    else:
        class_list.append(f)



# class_list.append(ab.name)
# class_list.append(ash.name)
# class_list.append(cal.name)
# class_list.append(col.name)
# class_list.append(dan.name)
# class_list.append(dav.name)
# class_list.append(dec.name)
# class_list.append(dev.name)
# class_list.append(dong.name)
# class_list.append(el.name)
# class_list.append(gar.name)
# class_list.append(gre.name)
# class_list.append(kam.name)
# class_list.append(kels.name)
# class_list.append(lauryn.name)
# class_list.append(mat.name)
# class_list.append(mor.name)
# class_list.append(noa.name)
# class_list.append(pat.name)
# class_list.append(spen.name)
# class_list.append(st.name)

print(class_list)