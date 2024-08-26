## 1. Introduction ##

from csv import reader

opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)[1:]

## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt

eg_1 = dt.datetime(1985, 3, 9)

print(eg_1)

eg_2 = dt.datetime(2019, 7, 25, 11, 27, 30)

print(eg_2)

ibm_founded = dt.datetime(1911, 6, 16)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)


## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it

# print(potus[-1][2])

eg_1 = str(potus[-1][2])
print(eg_1)

# eg_1 = eg_1.split()
# y_m_d = eg_1[0]
# h = eg_1[1]
# y_m_d = y_m_d.split('/')
# h = h.split(':')

# yr = int(y_m_d[2])

# print(yr)
# print(h)



date_format = '%m/%d/%y %H:%M'

for row in potus:
    appt_start_date = str(row[2])
    appt_start_date = dt.datetime.strptime(appt_start_date, date_format)
    row[2] = appt_start_date
    



## 6. Using Strftime to Format Dates ##

dt_object = dt.datetime(1985, 3, 9)
dia = dt_object.day
mes = dt_object.month
ano = dt_object.year
frase = 'O Belinho nasceu no dia {} ao mes {} do Glorioso ano de {}'.format(dia, mes, ano)

print(frase)

visitors_per_month = {}

for row in potus:
    data = row[2]
    data = data.strftime('%B, %Y')
    row[2] = data
    
    if data not in visitors_per_month:
        visitors_per_month[data] = 1
    else:
        visitors_per_month[data] += 1
    

## 7. The Time Class ##

a = dt.time(8, 15, 15)
print(a)

b = dt.datetime(1985, 3, 9, 15, 30)
b = b.time()
print(b)

time_str = '08:15'
time_dt = dt.datetime.strptime(time_str, '%H:%M')
print(time_dt)

time_dt = time_dt.time()
print(time_dt)

appt_times = []

for row in potus:
    date_time = row[2]
    date_time = date_time.time()
    appt_times.append(date_time)
        
print(appt_times)


                               

## 8. Comparing Time Objects ##

t1 = dt.time(0, 0)
t2 = dt.time(12, 0)

comparacao = t1 == t2
comparacao2 = t1 > t2
comparacao3 = t1 < t2

print(comparacao)
print(comparacao2)
print(comparacao3)

#tb poderemos usar as funções max e min nos ojectos de tempo:

tempo_varios = [dt.time(0,0),
                dt.time(12,0),
                dt.time(23,59),
                dt.time(8,15),
                dt.time(20,15)
               ]
print(max(tempo_varios))
print(min(tempo_varios))

min_time = min(appt_times)
max_time = max(appt_times)

print(min_time)
print(max_time)
                
             
          

## 9. Calculations with Dates and Times ##

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
print(type(answer_1))

answer_2 = dt_3 + dt.timedelta(days=56)
print(type(answer_2))

answer_3 = dt_4 - dt.timedelta(seconds=3600)
print(type(answer_3))

tres_semanas = dt.timedelta(6, 0, 0, 0, 0, 0, weeks=3)
print(tres_semanas)


## 10. Summarizing Appointment Lengths ##

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
    
    
appt_lengths = {}

for row in potus:
    appt_start_date = row[2]
    appt_end_date = row[3]
    length = appt_end_date - appt_start_date
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] += 1
        
min_length = min(appt_lengths)
max_length = max(appt_lengths)

print(min_length)
print(max_length)