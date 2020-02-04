def generate_hashtag(frase):
    if frase == "":
        return ""
    else:
        lista_frase = frase.split(' ')
        resultado = []
        for palabra in lista_frase:
            resultado.append(palabra.capitalize())
        resultado = "#" + "".join(resultado)
        if len(resultado) >= 140:
            return False
        else:
            return resultado


if __name__ == "__main__":

    assert generate_hashtag('') == ''
    assert generate_hashtag('Codewars') == '#Codewars'
    assert generate_hashtag('Codewars      ') == '#Codewars'
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'
    assert generate_hashtag('c i n') == '#CIN'
    assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False