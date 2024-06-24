import re

# Entrada do usuário
prompt_usuario = input()
prompt_palavras = re.findall(r'\b\w+\b', prompt_usuario.lower())
# Função para avaliar se o prompt está adequado
def avaliar_prompt(prompt_palavras):
    # Verifica se o prompt contém palavras-chave relevantes
    palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia" ]
    prompt_text = ' '.join(prompt_palavras)
    for palavra in palavras_chave:
        if palavra in ' '.join(prompt_palavras):
            return "O prompt está adequado."
    
    return "O prompt não está adequado. Inclua palavras-chave relevantes."

# Avaliar o prompt do usuário
feedback_usuario = avaliar_prompt(prompt_palavras)

# Exibir feedback
print(feedback_usuario)