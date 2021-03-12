from sly import Lexer, Parser

class CalcLexer(Lexer):
    #Lista de todos los tokens que se utilizaran
    tokens = {
        'PROGRAM',      #program
        'ID',           #id
        'SEMICOLON',     #;
        'COMMA',        #,
        'COLON',        #:
        'INT',          #cte int
        'FLOAT',        #cte float
        'STRING',       #cte string
        'L_CURPAR',     #{
        'R_CURPAR',     #}
        'EQ',           #=
        'LESS',         #<
        'GREATER',      #>
        'DIF',          #<>
        'L_PAR',        #(
        'R_PAR',        #)
        'IF',           #if
        'ELSE',         #else
        'VAR',          #var
        'PRINT',        #print
        'PLUS',         #+
        'MINUS',        #-
        'MULT',         #*
        'DIV'          #/
    }
    #Definicion de variables para los tokens
    ignore = ' \t'
    SEMICOLON = r'\;'
    COMMA = r'\,'
    COLON = r'\:'
    L_CURPAR = r'\{'
    R_CURPAR = r'\}'
    EQ = r'\='
    DIF = r'\<\>'
    LESS = r'\<'
    GREATER = r'\>'
    L_PAR = r'\('
    R_PAR = r'\)'
    PLUS = r'\+'
    MINUS = r'\-'
    MULT = r'\*'
    DIV = r'\/'
    PROGRAM = r'program'
    IF = r'if'
    ELSE = r'else'
    PRINT = r'print'
    VAR = r'[a-z][a-zA-Z_0-9]*'
    ID = r'[A-Z][a-zA-Z0-9]*'
    STRING = r'"[a-zA-Z0-9!@#$%^&*()]*"'
    #Funcion para el token FLOAT
    @_(r'\d+\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t
    #Funcion para el token INT
    @_(r'\d+')
    def INT(self, t):
        t.value = int(t.value)
        return t
    #Funcion contadora de lineas
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    #Funcion para manejar errores
    def t_error(self, t):
        print('Line: %d: Not valid character: %r' % (self.lineno, t.value[0]))
        self.index += 1

#Funcion para probar el escaner lexico
"""if __name__ == '__main__':
    data = '''
if else print + - * / gabo_125 Gabo 123 12.356
@
'''
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print(tok)"""
#_______________PARSER________________
class CalcParser(Parser):
    lexer = CalcLexer()
    tokens = lexer.tokens
    index = 1

    def __init__(self):
        self.names = { }
    #Definición de gramatica
    @_('PROGRAM ID SEMICOLON programT')
    def program(self, p):
        self.index += 1

    @_('vars programF',
       'programF')
    def programT(self, p):
        return p
    
    @_('bloque empty')
    def programF(self, p):
        return p

    @_('VAR varsT')
    def vars(self, p):
        return p

    @_('ID COMMA varsT',
       'ID COLON tipo SEMICOLON varsF')
    def varsT(self, p):
        return p

    @_('varsT',
       'empty')
    def varsF(self, p):
        return p

    @_('INT empty',
       'FLOAT empty')
    def tipo(self, p):
        return p

    @_('L_CURPAR bloqueT')
    def bloque(self, p):
        return p

    @_('estatuto bloqueT',
       'R_CURPAR  empty')
    def bloqueT(self, p):
        return p

    @_('asignacion empty',
       'condicion empty',
       'escritura empty')
    def estatuto(self, p):
        return p

    @_('ID EQ expresion SEMICOLON empty')
    def asignacion(self, p):
        return p

    @_('PRINT L_PAR escrituraT')
    def escritura(self, p):
        return p

    @_('expresion escrituraF',
       'STRING escrituraF')
    def escrituraT(self, p):
        return p

    @_('COMMA  escrituraT',
       'R_PAR SEMICOLON empty')
    def escrituraF(self, p):
        return p

    @_('exp expresionT')
    def expresion(self, p):
        return p

    @_('LESS exp empty',
       'GREATER exp empty',
       'DIF exp empty',
       'empty')
    def expresionT(self, p):
        return p

    @_('IF L_PAR expresion R_PAR bloque condicionT')
    def condicion(self, p):
        return p

    @_('ELSE bloque empty',
       'empty')
    def condicionT(self, p):
        return p

    @_('termino expT')
    def exp(self, p):
        return p

    @_('PLUS exp',
       'MINUS exp',
       'empty')
    def expT(self, p):
        return p

    @_('factor terminoT')
    def termino(self, p):
        return p

    @_('MULT termino',
       'DIV termino',
       'empty')
    def terminoT(self, p):
        return p

    @_('L_PAR expresion R_PAR empty',
       'factorT')
    def factor(self, p):
        return p

    @_('PLUS factorF',
       'MINUS factorF',
       'factorF')
    def factorT(self, p):
        return p

    @_('varcte empty')
    def factorF(self, p):
        return p

    @_('ID empty',
       'INT empty',
       'FLOAT empty')
    def varcte(self, p):
        return p

    @_(' ')
    def empty(self, p):
        return p
    #Función para manejar errores
    def error(self, p):
        if p:
            print("Syntax error at line: %d, index: %d" % (self.index, p.index))
            self.index += 1
            self.tokens
        else:
            print("Syntax error at EOF")

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
try:
    f = open("pruebas.txt", "r")
    for s in f:
        parser.parse(lexer.tokenize(s))
    
except EOFError:
    print('Error')
            