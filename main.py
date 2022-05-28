import csv 

filename = "./clgs.csv"

data = []

with open(filename, 'r') as f:
    csv_data = csv.reader(f)

    institute_code = "" #1
    clg_name = "" #2
    dept = "" #3
    city = "" #4
    autonomous = "" #5
    fees = "" #15

    for rows in csv_data:

        if len(rows[1]) == 0:
            rows[1] = institute_code
        if len(rows[2]) == 0:
            rows[2] = clg_name
        if len(rows[3]) == 0:
            rows[3] = dept
        if len(rows[4]) == 0:
            rows[4] = city
        if len(rows[5]) == 0:
            rows[5] = autonomous
        if len(rows[15]) == 0:
            rows[15] = fees

        institute_code = rows[1]
        clg_name = rows[2]
        dept = rows[3]
        city = rows[4]
        autonomous = rows[5]
        fees = rows[15]
        if "+" in rows[8]:
            
            sc,nt = rows[8].split("+")
            rows[8] = sc
            rows.insert(9, nt)
        else:
            rows[8] = rows[8]
            rows.insert(9, rows[8])
            
        data.append(rows)


new_filename = "final_clg.csv"

with open(new_filename, 'w', newline='', encoding='utf-8') as f:
    
    writer = csv.writer(f, delimiter=",")
    data[0][8] = "vac_sc"
    data[0].insert(9, "vac_nt")
    writer.writerow(data[0])
    writer.writerows(data[1:])
    


