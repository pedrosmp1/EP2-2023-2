def filtra(lista, num):
    especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    filtradas = []
    for palavra in lista:
        palavra = palavra.lower()
        for especial in especiais:
            palavra = palavra.replace(especial, '')
        if len(palavra) == num and palavra not in filtradas:
            filtradas.append(palavra)
    return filtradas
