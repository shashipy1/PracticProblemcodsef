
s= "HS08TEST, INTEST, FLOW001, START01, FLOW006, FLOW002, FCTRL2, FLOW004, FLOW007, FSQRT, DIFFSUM, CHOPRT, FLOW018, FLOW008, DECINC, FLOW013, PALL01, VOWELTB, SNCKYEAR, AREAPERI, FLOW011, REMISS, RECTANGL, FLOW009, HOWMANY, THREEFR, FLOW010, TEST, NUMGAME2, ODDEVENX, PPSUM, FLOW017, TRISQ"
ques_codes = s.split(",")

ques_codes = [q.lstrip() for q in ques_codes]

# print(ques_codes)
ques_codes[:5]
with open("my_codechef_practics_problem","a") as f:
    f.write('''<table style="border-collapse: collapse; width:50%;"border="2>\n<tbody>\n''')
    for i, q in enumerate(ques_codes):
        f.write(f'''<tr style="height: 50px;">
<td style="width: 10%; text-align: center; height: 40px;">{i+1}.</td>\n<td style="width: 20%; height: 40px; text-align: center;"><a href="https://www.codechef.com/problems/{q}">{q}</a></td>\n</tr>\n''')
    f.write("</tbody>\n</table>")