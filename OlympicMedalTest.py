import numpy as np

#create dataset as follows
olympic_country = np.array(['GBR','CHN','RUS','US','KOR','JPN','GER'])
olympic_country_gold = np.array([29,38,24,46,13,7,11])
olympic_country_silver = np.array([17,28,25,28,8,14,11])
olympic_country_bronze = np.array([19,22,32,29,7,17,14])

gold_argmax  = np.argmax(olympic_country_gold)
silver_argmax = np.argmax(olympic_country_silver)
bronze_argmax = np.argmax(olympic_country_bronze)

print('Country won max Gold is:',olympic_country[gold_argmax])
#print('Country won max ilver is:',olympic_country[silver_argmax])
#print('Country won max Bronze is:',olympic_country[bronze_argmax])

print('Countries who won more than 20 Gold medals are:')
print(olympic_country[olympic_country_gold>20])

total_medals = olympic_country_gold+olympic_country_silver+olympic_country_bronze
print('\nTotal medals are:',sum(total_medals))

print('\nCountries who won Gold medals are:')
for cnt in range(len(olympic_country_gold)):
	print(olympic_country[cnt])

print('\nMedals for each Country are:')
for i in range(len(total_medals)):
	print('Total Medals won by country',olympic_country[i],'is: ',total_medals[i],', Gold medal Won is: ',olympic_country_gold[i])