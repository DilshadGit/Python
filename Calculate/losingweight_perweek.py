import datetime

current_weight = 318

achive_weight = 71

avg_loss_per_week = 0.6

start_date = datetime.date.today()
end_date = start_date

while current_weight > achive_weight:
	end_date += datetime.timedelta(days=7)
	print(end_date)
	current_weight -= achive_weight

print(end_date)
print('Reached achivment in {} weeks'.format((end_date - start_date).days // 7))
# print(f'Reached achivment in {(end_date - start_date).days // 7} weeks')

