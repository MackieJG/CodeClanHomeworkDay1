age_gk = 31
age_rb = 30
age_rcb = 33
age_lcb = 29
age_lb = 30
age_rm = 23
age_rcm = 24
age_lcm = 27
age_lm = 27
age_rf = 28
age_lf = 26

total_goalkeeper_age = age_gk
total_defender_age = age_rb + age_rcb + age_lcb + age_lb
total_midfielder_age = age_rm + age_rcm + age_lcm + age_lm
total_attacker_age = age_rf + age_lf

total_squad_age = total_goalkeeper_age + total_defender_age + total_midfielder_age + total_attacker_age
average_squad_age = total_squad_age / 11

print(average_squad_age)
