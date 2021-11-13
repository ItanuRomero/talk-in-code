def print_structure(natural_text: str):
    content = natural_text.split('print ')[1]
    return f"print('{content}')"