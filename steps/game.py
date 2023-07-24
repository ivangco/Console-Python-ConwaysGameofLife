from behave import given, when, then

@given('que el juego ha comenzado')
def step_impl(context):
    # Puedes realizar tareas de configuración aquí si es necesario
    pass

@when('creo un tablero vacío de {width:d}x{height:d}')
def step_impl(context, width, height):
    # Implementa el código para crear un tablero vacío de tamaño width x height
    pass

@then('el tablero debe estar vacío')
def step_impl(context):
    # Implementa la aserción para verificar que el tablero está vacío
    pass

@when('coloco una célula viva en la posición ({x:d}, {y:d})')
def step_impl(context, x, y):
    # Implementa el código para colocar una célula viva en la posición (x, y) del tablero
    pass

@then('el tablero debe tener una célula viva en la posición ({x:d}, {y:d})')
def step_impl(context, x, y):
    # Implementa la aserción para verificar que el tablero tiene una célula viva en la posición (x, y)
    pass
