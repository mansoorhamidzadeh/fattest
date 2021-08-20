st='Braund, Mr. Owen Harris'

def f(name):
    if '.'  in  name:
        return name.split(',')[1].split('.')[0].strip()
    else :
        return "un"

print(f(st))