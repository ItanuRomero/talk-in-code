from talk_in_code import pt_translator
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("print fala pessoal", "print('fala pessoal')"),
    ("print sou eu", "print('sou eu')"),
    ("print alguma coisa", "print('alguma coisa')")
])
def test_print_structure(test_input, expected):
    assert expected == pt_translator.print_structure(test_input)


@pytest.mark.parametrize("test_input,expected", [
    ("variável nome recebe string itanu", "nome = str('itanu')"),
    ("variável idade recebe inteiro 20", "idade = int('20')"),
    ("variável altura recebe flutuante 2.30", "altura = float('2.30')")
])
def test_declare_variable(test_input, expected):
    assert expected == pt_translator.declare_variable(test_input)