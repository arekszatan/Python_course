# Oblicz wskaźnik BMI
# 18.5 < BMI < 24.9
# wzór (wzrost w metrach np. 1.7)
# bmi = masa / (wzrost * wzrost)
#
# Oblicz bmi według powyższego wzoru dla wagi 94
# i wzrostu 1.75, pokaż wyniki w koonsoli

height = 1.9
mass = 94
bmi = mass / (height * height)
print(f'BMI: {bmi} for height {height} and mass {mass}')
print(type(bmi))