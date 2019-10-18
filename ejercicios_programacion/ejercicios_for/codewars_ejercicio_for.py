def duplicate_encode(word):
    wordEncoded = ""
    for caracter in word:
        if caracter.count(word) == 1:
            wordEncoded = wordEncoded + "("
        else:
            wordEncoded = wordEncoded + ")"
    return wordEncoded


if __name__ == "__main__":

    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("
