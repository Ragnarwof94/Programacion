"""
Comentrario
de
multiples
lineas
"""
" ➡️ Este bloque es una cadena de texto multilínea creada con comillas triples (""").
" 📌 Python no la trata como comentario.

" Si está suelta (como aquí), el intérprete la ignora, porque no se asigna a ninguna variable ni se usa.

" En la práctica, mucha gente la usa como comentario multilínea, pero técnicamente es un string.

"💡 Realmente se usan para docstrings (documentación oficial en funciones, clases o módulos).


'''
Comentrario
de
multiples
lineas
'''
# ➡️ Lo mismo que el anterior, pero con comillas triples simples (''').
# 👉 Sigue siendo una cadena multilínea sin uso → Python no hace nada con ella.

# ⚠️ Explicación importante
# 🔴 No existen comentarios multilínea reales en Python.
# Solo hay comentarios de una línea usando #.

# ✔️ Las comillas triples sirven para:

# Documentación interna (docstrings)

# Strings largos

# Plantillas de texto

# Ejemplo correcto de docstring
def sumar(a, b):
    """
    Esta función recibe dos números
    y retorna la suma de ambos.
    """
    return a + b
" 👉 Aquí sí tiene un propósito: documentar la función.
" Este texto aparece en herramientas como help(), IDEs, etc.