def print_structure(natural_text: str):
    content = natural_text.split('print ')[1]
    return f"print('{content}')"


def declare_variable(natural_text: str):
    types = {
        'string': 'str',
        'inteiro': 'int',
        'flutuante': 'float',
        'booleano': 'bool',
        'complexo': 'complex',
        'lista': 'list',
        'objeto': 'object'
    }
    content = natural_text.split('variável ')[1]
    name, type_and_value = content.split('recebe ')
    name = name.strip()
    type_of, value = type_and_value.split(' ')
    type_of = types[type_of]
    code = f"{name} = {type_of}('{value}')"
    return f"{code}"
