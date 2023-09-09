import string
import random

all_characters = [
    string.digits,
    string.punctuation,
    string.ascii_lowercase,
    string.ascii_uppercase,
]
sifre = ""
uz = int(
    input(
        "pasword lenght (girdiniz rakamın 2 katı olur ör 4 rakamının sifre uzunluğu 8): "
    )
)
for j in range(uz):
    for i in range(2):
        sifre += all_characters[i][random.randint(0, 9)]
sifre = list(sifre)
random.shuffle(sifre)
ana_sifre = ""
ana_sifre = ana_sifre.join(sifre)
print(ana_sifre)
