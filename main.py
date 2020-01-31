from sugar_lists import sugar_class
import pandas as pd
import xlsxwriter
import string
import xlrd


sugar_processor = sugar_class()



def find_sugar(ingreientsList):
    sugar_word_list = []
    count = 1
    for i in ingreientsList:
        if isinstance(i, float) == False:
            sugarList = []
            ingList = i.split("-")
            for sugar_word in sugar_processor.sweeteners_list:
                for x in ingList:
                    if sugar_word.lower() in x.lower():
                        sugarList.append(x)
            sugar_word_list.append(sugarList)
            count += 1
    return sugar_word_list, count

def find_linked_recipes():
    Ahfinal = ("databases/ah_dutch_desserts_cat_final.xlsx")
    arafinal = ("databases/arabicfinal.xlsx")
    wbf = xlrd.open_workbook(Ahfinal)
    sheetf = wbf.sheet_by_index(0)
    wbo = xlrd.open_workbook(arafinal)
    sheeto = wbo.sheet_by_index(0)
    for i in range(1, 101, 1):
        for x in range(1, 249, 1):
            if sheeto.cell_value(i, 0) == sheetf.cell_value(x, 0):  # If both recipes have the same linking ID print
                print(sheeto.cell_value(i, 1),sheetf.cell_value(x, 1))    #arabic serving, Dutch serving

def write_into_excel(listLists):
    workbook = xlsxwriter.Workbook('databases\sugarara0.xlsx')
    worksheet = workbook.add_worksheet()
    count = 1
    for i in listLists:
        titleexc = 'A' + str(count)
        worksheet.write(titleexc, "%s\n" % ",\n".join(i))
        count +=1
    workbook.close()

def find_none_repetitive_sugar_list(m):
    none_repetitive = []
    for i in m:
        for z in i:
            suList = z.split(":")
            exclude = set(string.punctuation)
            s = ''.join(ch for ch in suList[0] if ch not in exclude)
            if s not in none_repetitive:
                none_repetitive.append(s)
    return none_repetitive

def main():
    df = pd.read_excel('databases/arabicfinal.xlsx', usecols = ["ingredients"])   # ingredients    ah_dutch_desserts_cat_final   arabicfinal
    inglist = df["ingredients"].values
    sugar_list = find_sugar(inglist)[0]
    write_into_excel(sugar_list)
    find_none_repetitive_sugar_list(sugar_list)


if __name__ == "__main__":
    main()

