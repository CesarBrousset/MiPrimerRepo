# class Perro:
#    postura = "cuadrúpedo"

#    def __init__(self, nombre, raza):
#        self.nombre = nombre.capitalize()
#        self.raza = raza

#    def ladrar(self):
#        print("arrrgg... Guau Guau")

#    def caminar(self, pasos):

#        print(f"camina {pasos} pasos")


# mi_perro = Perro("patan", "chihuahua")
# mi_perro.postura

# print(f"Su nombre es:\n{mi_perro.nombre}")
# print(f"Su raza es:\n{mi_perro.raza}")
# print(f"Es un {mi_perro.postura}")
# mi_perro.caminar(6)
# mi_perro.ladrar()

# class Persona:
#    postura = 'bípeda'
#    animal = 'racional'

#    def __init__(self, nombre, domicilio, profesion):
#        self.nombre = nombre
#        self.domicilio = domicilio
#        self.profesion = profesion

#    def caminar(self, pasos):
#        print(f'El individuo camina {pasos} pasos')

#    def hablar(self, idioma):
#        print(f'el individuo habla el idioma {idioma}')

# primer_persona = Persona('César', 'Córdoba', 'Abogado')

# print(f'Su nombre es:\n{primer_persona.nombre}')
# print(f'Vive en:\n{primer_persona.domicilio}')
# print(f'Su profesión es:\n{primer_persona.profesion}')
# primer_persona.caminar(1257)
# primer_persona.hablar('español')

# segunda_persona = Persona ('Paulina', 'Arroyito', 'no tiene')

# print(f'Su nombre es:\n{segunda_persona.nombre}')
# print(f'Vive en:\n{segunda_persona.domicilio}')
# print(f'Su profesión es:\n{segunda_persona.profesion}')
# segunda_persona.caminar(125)
# segunda_persona.hablar('español')


class Atleta:
    def __init__(self, nombre, apellido, peso, altura, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.peso = peso
        self.altura = altura
        self.__telefono = telefono

    def __str__(self):
        return f"los datos son: {self.nombre, self.apellido, self.peso, self.altura}"

    #def __iter__(self):
    #    for pos in self.calcularIMC():
    #        yield f"Value[{pos}] : {self.calcularIMC(pos)}]"

    def calcularIMC(self):
        imc = self.peso / (self.altura**2)
        if imc < 18.5:
            print("Peso inferior")
        elif imc >= 18.5 and imc <= 24.9:
            print("Peso normal")
        elif imc >= 25 and imc <= 29.9:
            print("Sobrepeso")
        elif imc >= 30 and imc <= 34.9:
            print("Obesidad")
        else:
            print("Obesidad extrema")

    # def __getitem__(self, pos1):
    #    return self.__telefono[pos1]

    # def __getitem__(self, pos2):
    #    return self.nombre[pos2]
    # def __setitem__(self, pos2, nombre):
    #    self.nombre[pos2] =  nombre


primer_encuestado = Atleta("Cesar", "Brousset", 88, 1.88, 3516366743)
print(primer_encuestado)
primer_encuestado.calcularIMC()
