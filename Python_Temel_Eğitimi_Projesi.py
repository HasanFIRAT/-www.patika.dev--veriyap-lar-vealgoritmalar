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
