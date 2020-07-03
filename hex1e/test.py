from datetime import date, datetime

date_lowertax_begin = date(2020,7,1)
date_lowertax_end = date(2020,12,31)
lowertax_applies = date_lowertax_begin <= date(2020,6,30) <=date_lowertax_end
now = datetime.now()
tax_multiplier = 0.16 if lowertax_applies else 0.19
print(tax_multiplier)
