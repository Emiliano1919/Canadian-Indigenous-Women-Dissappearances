import tabula
for i in range(52):
    name = "output"+str(i+1)+".csv"
    page =i+1
    tabula.convert_into("Pearce_Maryanne_2013_Thesis.pdf", name, output_format="csv", pages=str(page))