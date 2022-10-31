# Python_Temel_Eğitimi_Projesi

def flatten_list(in_list, out_list):
    for item in in_list:
        if type(item) is list:
            flatten_list(item, out_list)
        else:
            out_list.append(item)
l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
o=[]
flatten_list(l, o)
print(o)

def ters_list(in_list, out_list):
    for i in in_list:
        if type(i) is list:
            i=i[::-1]
            out_list.append(i)
        else:
            out_list.append(i)

liste=[[1, 2], [3, 4], [5, 6, 7]]
ters_liste=[]
ters_list(liste, ters_liste)
ters_liste=ters_liste[::-1]
print(ters_liste)