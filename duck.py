import ply.lex as lex
import ply.yacc as yacc
import sys

#Lista de todos los tokens que se utilizaran
tokens = [

    'PROGRAM',      #program
    'ID',           #id
    'SEMICOLON',     #;
    'DOT',          #.
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
    'DIV',          #/
]
#Definicion de variables para los tokens
t_SEMICOLON = r'\;'
t_DOT = r'\.'
t_COMMA = r'\,'
t_COLON = r'\:'
t_L_CURPAR = r'\{'
t_R_CURPAR = r'\}'
t_EQ = r'\='
t_DIF = r'\<\>'
t_LESS = r'\<'
t_GREATER = r'\>'
t_L_PAR = r'\('
t_R_PAR = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'

t_ignore = r' \t'

def t_PROGRAM(t):
    r'program'
    t.type = 'PROGRAM'
    return t

def t_IF(t):
    r'if'
    t.type = 'IF'
    return t

def t_ELSE(t):
    r'else'
    t.type = 'ELSE'
    return t 

def t_PRINT(t):
    r'print'
    t.type = 'PRINT'
    return t 

def t_VAR(t):
    r'[a-z][a-zA-Z_0-9]*'
    t.type = 'VAR'
    return t

def t_ID(t):
    r'[A-Z][a-zA-Z0-9]*'
    t.type = 'ID'
    return t

def t_FLOAT(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[a-zA-Z0-9!@#$%^&*()]*"'
    t.type = 'STRING'
    return t
#Variable para manejar errores de 0 coincidencias 
def t_error(t):
    print('Not valid character: %s' % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#Funcion para probar el escaner lexico 
def pruebaLex():
    lexer.input("if else print + - * / gabo_125 Gabo")

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
