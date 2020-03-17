# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106061135.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:
      data.append(row)

#=======================================

# Part. 3

#=======================================

target_data0 = list(filter(lambda item: item['station_id'] == 'C0A880', data))
target_data1 = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
target_data2 = list(filter(lambda item: item['station_id'] == 'C0G640', data))
target_data3 = list(filter(lambda item: item['station_id'] == 'C0R190', data))
target_data4 = list(filter(lambda item: item['station_id'] == 'C0X260', data))

value0 = []
value1 = []
value2 = []
value3 = []
value4 = []

for i in range(len(target_data0)):
   value0.append(i)
   if((target_data0[i]['WDSD'] == '-99.000') | (target_data0[i]['WDSD'] == '-999.000')):
      value0[i] = 0.499
   else:
      value0[i] = target_data0[i]['WDSD']
for i in range(len(target_data1)):
   value1.append(i)
   if((target_data1[i]['WDSD'] == '-99.000') | (target_data1[i]['WDSD'] == '-999.000')):
      value1[i] = 0.499
   else:
      value1[i] = target_data1[i]['WDSD']
for i in range(len(target_data2)):
   value2.append(i)
   if((target_data2[i]['WDSD'] == '-99.000') | (target_data2[i]['WDSD'] == '-999.000')):
      value2[i] = 0.499
   else:
      value2[i] = target_data2[i]['WDSD']

for i in range(len(target_data3)):
   value3.append(i)
   if((target_data3[i]['WDSD'] == '-99.000') | (target_data3[i]['WDSD'] == '-999.000')):
      value3[i] = 0.499
   else:
      value3[i] = float(target_data3[i]['WDSD'])
for i in range(len(target_data4)):
   value4.append(i)
   if((target_data4[i]['WDSD'] == '-99.000') | (target_data4[i]['WDSD'] == '-999.000')):
      value4[i] = 0.499
   else:
      value4[i] = target_data4[i]['WDSD'] 

max_value0 = max(value0)
min_value0 = min(value0)
max_value1 = max(value1)
min_value1 = min(value1)
max_value2 = max(value2)
min_value2 = min(value2)
max_value3 = max(value3)
min_value3 = min(value3)
max_value4 = max(value4)
min_value4 = min(value4)

x0 = float(max_value0) - float(min_value0)
x1 = float(max_value1) - float(min_value1)
x2 = float(max_value2) - float(min_value2)
x3 = float(max_value3) - float(min_value3)
x4 = float(max_value4) - float(min_value4)
if( x0 == 0) :
   x0 = 'None'
elif (max_value0 == 0.499):
   x0 = 'None'
elif (min_value0 == 0.499):
   x0 = 'None' 

if( x1 == 0):
   x1 = 'None'
elif (max_value1 == 0.499):
   x1 = 'None'
elif (min_value1 == 0.499):
   x1 = 'None'

if( x2 == 0):
   x2 = 'None'
elif (max_value2 == 0.499):
   x2 = 'None'
elif (min_value2 == 0.499):
   x2 = 'None'

if( x3 == 0):
   x3 = 'None'
elif (max_value3 == 0.499):
   x3 = 'None'
elif (min_value3 == 0.499):
   x3 = 'None'

if( x4 == 0):
   x4 = 'None'  
elif (max_value4 == 0.499):
   x4 = 'None'
elif (min_value4 == 0.499):
   x4 = 'None'

print('[[',target_data0[0]['station_id'],',',x0,']',
      '[',target_data1[0]['station_id'],',',x1,']',
      '[',target_data2[0]['station_id'],',',x2,']',
      '[',target_data3[0]['station_id'],',',x3,']',
      '[',target_data4[0]['station_id'],',',x4,']]')

