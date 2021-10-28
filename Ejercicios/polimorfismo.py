# Ejemplo práctico sobre Polimorfismo en Python.

class Radio:
    def __init__(self, status):
        self.status = status
    
    def plan(self):
      '''
      Función que muestra la cabecera según el estado de la cuenta
      que son: plan gratuito o premium
      '''
        if self.status == False:
            print("--- Música gratis ---")
        elif self.status ==  True:
            print("--- Música Premium ---")
             
class FreeMusic(Radio):
    def __init__(self, status):
        super().__init__(status)
    
    def plan(self):
      '''
      Función heredada de la clase Radio que muestra información
      según si el plan está activo o no. (Polimorfismo)
      '''
        count = 0
        upgrade = ['Música sin publicidad', 'Miles de canciones', 'Descarga tu lista favorita']
        if self.status == False:
            print('Te recomendamos suscribirte al plan Premium:')
            for item in upgrade:
                count += 1
                print(count, item)

class PremiumMusic(Radio):
    def __init__(self, status):
        super().__init__(status)
    
    def plan(self):
         '''
         Función heredada de la clase Radio que al igual que la clase FreeMusic,
         muestra información según si el plan está activo o no. (Polimorfismo)
         '''
        if self.status == True:
            print('¡Disfruta del plan Premium!')

# Llamada al objeto
active = Radio(True)

# Activa el plan según el satus 
if active.status != True:
    active.plan()
    free_function = FreeMusic(False)
    free_function.plan()
elif active.status == True:
    active.plan()
    premium_function = PremiumMusic(True)
    premium_function.plan()
