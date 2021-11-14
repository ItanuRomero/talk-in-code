import pt_translator


def from_pt(natural_text: str):
    if natural_text.split(' ')[0] == 'print':
        code = pt_translator.print_structure(natural_text)
    elif natural_text.split(' ')[0] == 'variável':
        code = pt_translator.declare_variable(natural_text)
    return code


def run(natural_text: str, language='pt-BR'):
    if language == 'pt-BR':
        code = from_pt(natural_text)
    return code


if __name__ == '__main__':
    code_line = run('variável x recebe string itanu')
    print(code_line)
