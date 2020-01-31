import xlrd
from sugar_lists import sugar_class
soorten_suiker = sugar_class()

# Give the location of the file
arafinal = ("databases/ah_dutch_desserts_cat_final.xlsx")
# To open Workbook
wbo = xlrd.open_workbook(arafinal)
sheeto = wbo.sheet_by_index(0)

for i in range(0, 89, 1):
    x = sheeto.cell_value(i, 0).split(",")
    final_sugar = 0
    for z in x:
        ing = []
        h = z.replace('\n','')
        y = h.split(":")
        f = ""
        new_title = ""
        for w in y[-1]:
            if w.isdigit() == True or w == ".":
                f += w
        if f == '':
            pass
        else:
            f = round(float(f))
            if len(y[0])> 0 and y[0][0] == " ":
                new_title = y[0][1:]
                ing.append(new_title.lower())
            else:
                ing.append(y[0].lower())
        ing.append(f)
        ing.append("g")
        #print(ing)
        if len(ing)>2:
            final_sugar += soorten_suiker.amount_of_sugar(ing)
    print(round(final_sugar))
    #print("*********")
