def month_to_season(num):
	if 1 <= num >= 2 or num == 12:
		return("Зима")
	if 3 <= num >= 5:
		return("Весна")
	if 6 <= num >= 8:
		return("Лето")
	if 9 <= num >= 11:
		return("Осень")
print(month_to_season(2))