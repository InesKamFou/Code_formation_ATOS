from datetime import datetime, date, time, timedelta
#import time

now = datetime.now()
print(now)
# time.sleep(3)
# now = datetime.now()
# print(now)
today = date.today()
print(today)

current_time = datetime.now().time()
print(current_time)
current_date = datetime.now().date() # équivalent à today = date.today()
print(current_date)

# Créer une date
d = date(2026,2,1)
print(d)
t = time(17,0)
print(t)
dt = datetime(2026,2,20,17,0)
print(dt)

# Formater une date -> texte (strftime)

formated = now.strftime("%y-%B-%d")
print(f"La date formatée: {formated}")

# formater texte -> date
text_date ="2026-02-20 14:28:00"
parsed = datetime.strptime(text_date, '%Y-%m-%d %H:%M:%S')
print(type(parsed), parsed)

text_date ="2026/02/20 14:28:00"
parsed = datetime.strptime(text_date, '%Y/%m/%d %H:%M:%S')
print(type(parsed), parsed)

text_date ="2026/February/20 14:28:00"
parsed = datetime.strptime(text_date, '%Y/%B/%d %H:%M:%S')
print(type(parsed), parsed)

# Calcuer des délais
delta = timedelta(days = 3, hours=3)
future_heure = now + delta
print(future_heure)

naissance = datetime(1979, 1,24, 11,00)
age_jour = now - naissance
print(age_jour)

jour = datetime(1979, 1,1)
print(naissance >jour) # plus récent

date1 = '2001-01-17 06:26:40.000'
date1 = date1[:10]
date_1 = datetime.strptime(date1, '%Y-%m-%d')
print(date_1.date())
date2= '03/11/2006 09:20'
date2 = date2[:10]
date_2 = datetime.strptime(date2, '%d/%m/%Y')
print(date_1-date_2)
