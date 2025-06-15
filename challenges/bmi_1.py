# Zadanie: Kalkulator BMI z funkcją
#
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję calculateBMI, która przyjmuje wagę w kilogramach i zrost w centymetrach.
# Funkcja powinna obliczać BMI i zwracać wartość BMI według wzoru:
# weight / ((height / 100) ** 2)
# 2) Zdefiniuj funkcję classifyBMI, która przyjmuję wartość BMI i klasyfikuję ją
# do odpowiedniego przedziału.
# bmi < 18.5 z info: Masz niedowagę
# bmi < 25 z info: Twoja waga jest w normie.
# bmi < 30 z info: Masz nadwagę.
# reszta wartości to: "Masz sporą nadwagę."
# 3) Poproś użytkownika o wprowadzenie wagi i wzrostu.
# 4) Wywołaj funkcję calculateBMI, aby obliczyć BMI na podstawie danych użytkownika.
# 5) Wywołaj funkcję classifyBMI, aby określić przedział BMI i wyświetlić odpowiedni komunikat.

def calculate_BMI(weight, height) -> float:
    return weight / ((height / 100) ** 2)

def classify_BMI(_bmi):
    if _bmi < 18.5:
        return "Masz niedowagę"
    elif _bmi < 25:
        return "Twoja waga jest w normie."
    elif _bmi < 30:
        return "Masz nadwagę."
    else:
        return "Masz sporą nadwagę."

if __name__ == '__main__':
    print("Start programu.")
    weight_input = float(input("Proszę podaj aktualną wagę: "))
    height_input = float(input("Proszę podaj aktualny wzrost: "))
    bmi = calculate_BMI(weight_input, height_input)
    print("Twoje BMI jest równe: " + str(bmi) + " , a komunikat to: " + classify_BMI(bmi))