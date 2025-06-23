# Zadnie String replace
# 1) Stwórz funkcję clean_text, która będzie czyścić
# przekazany tekst z określonych słów.
# 2) Użyj funkcji replace do zmiany podanych słów na
# wykropkowany, które wielokrotnie może pojawić się
# w przekazanym łańcuchy. Dla uproszczenia będziesz
# zamieniać nazwy łańcuchów programowania ;) np.
# php zamienisz na ***, java na **** itd.
# 3) Zastąp następujące słowa kluczowe:
# JavaScript, java, php, html, css
# 4) Zwróć wyczyszczony tekst z funkcji clean_text.
# 5) Wywołaj funkcję na następującym lub podobnym tekście:
# """Programowanie zacząłem z językiem php, następnie
# poznałem: html i css, ale obecnie skupiam się na
# JavaScript"""
# Wynik pokaż w konsoli.

def clean_text(text):
    words_to_replace = ["php", "java", "html", "css", "JavaScript"]
    for word in words_to_replace:
        text = text.replace(word, "*" * len(word))
    return text

string_test = """Programowanie zacząłem z językiem php, następnie
poznałem: html i css, ale obecnie skupiam się na 
JavaScript"""

result = clean_text(string_test)
print(result)

