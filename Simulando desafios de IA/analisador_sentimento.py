# Importa o módulo re, que é a biblioteca de expressões regulares do Python. 
import re

def analyze_sentiment():
    # Entrada do usuário
    comentario = input()

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    # Lista de palavras positivas, negativas e neutras
    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)

    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    elif count_negativo > count_positivo and count_neutro == 0:
        return "Negativo"
    else:
        return "Neutro"
    
sentimento = analyze_sentiment()
print("Sentimento:", sentimento)