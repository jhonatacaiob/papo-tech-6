from rich.console import Console
from rich.table import Table

table = Table(
    title='Nomes de métodos especiais (excluindo operadores)',
    show_lines=True,
    highlight=True,
)

table.add_column('Categoria', justify='center')
table.add_column('Nomes dos métodos')

table.add_row(
    'Representação de string/bytes',
    '__repr__  __str__  __format__  __bytes__  __fspath__',
)
table.add_row(
    'Conversão para número',
    '__bool__  __complex__  __int__  __float__  __hash__  __index__',
)
table.add_row(
    'Iteração', '__iter__  __aiter__  __next__  __anext__  __reversed__'
)
table.add_row('Execução de chamável ou corrotina', '__call__  __await__')
table.add_row(
    'Gerenciamento de contexto', '__enter__  __exit__  __aexit__  __aenter__'
)
table.add_row(
    'Criação e destruição de instâncias', '__new__  __init__  __del__'
)
table.add_row(
    'Gerenciamento de atributos',
    '__getattr__  __getattribute__  __setattr__  __delattr__  __dir__',
)
table.add_row(
    'Descritores de atributos', '__get__  __set__  __delete__  __set_name__'
)
table.add_row('Classes base abstratas', '__instancecheck__  __subclasscheck__')
table.add_row(
    'Metaprogramação de classes',
    '__prepare__  __init_subclass__  __class_getitem__  __mro_entries__',
)


table2 = Table(
    title='Nomes e símbolos de métodos especiais para operadores',
    show_lines=True,
    highlight=True,
)
table2.add_column('Categoria do operador')
table2.add_column('Símbolos')
table2.add_column('Nomes de métodos')


table2.add_row('Unário numérico', '-  +  abs()', '__neg__  __pos__  __abs__')
table2.add_row(
    'Comparação rica',
    '<  <=  ==  !=  >  >=',
    '__lt__  __le__  __eq__  __ne__  __gt__  __ge__',
)
table2.add_row(
    'Aritmético',
    '+  -  *  /  //  %  @  divmod()  round()  **  pow()',
    '__add__  __sub__  __mul__  __truediv__  __floordiv__  __mod__  __matmul__  __divmod__  __round__  __pow__',
)
table2.add_row(
    'Aritmética reversa',
    'operadores aritméticos com operandos invertidos)',
    '__radd__  __rsub__  __rmul__  __rtruediv__  __rfloordiv__  __rmod__  __rmatmul__  __rdivmod__  __rpow__',
)
table2.add_row(
    'Atribuição aritmética aumentada',
    '+=  -=  *=  /=  //=  %=  @=  **=',
    '__iadd__  __isub__  __imul__  __itruediv__  __ifloordiv__  __imod__  __imatmul__  __ipow__',
)
table2.add_row(
    'Bit a bit',
    '&  |  ^  <<  >>  ~',
    '__and__  __or__  __xor__  __lshift__  __rshift__  __invert__',
)
table2.add_row(
    'Bit a bit reversa',
    '(operadores bit a bit com os operandos invertidos)',
    '__rand__  __ror__  __rxor__  __rlshift__  __rrshift__',
)
table2.add_row(
    'Atribuição bit a bit aumentada',
    '&=  |=  ^=  <⇐  >>=',
    '__iand__  __ior__  __ixor__  __ilshift__  __irshift__',
)


console = Console()
console.print(table)
console.print(table2)
