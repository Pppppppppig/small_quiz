import re

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
end = dict()
sub_fund = list()
rtxt = re.split('\d{1}\. ', long_text)
rtxt_0 = [i for i in rtxt.pop(0).split('\n') if i]
end['name'] = rtxt_0[0]
end['lei'] = rtxt_0[1]
for te in rtxt:
    sub_fund_temp = dict()
    temp = [i for i in te.split('\n') if i]
    sub_fund_temp['title'] = temp.pop(0)
    sub_fund_temp['isin'] = temp
    sub_fund.append(sub_fund_temp)
end['sub_fund'] = sub_fund

print(end)
