# Solución del Parcial Corte 1

## Paso a Paso del ejercicio estructural

El código presentaba un error en su último `print`, que era:

```python
print(maximo(nums)

Para solucionarlo, solo era necesario cerrar correctamente la instrucción del print, quedando así:

print(maximo(nums))

Paso a Paso del ejercicio de OOP

El código presentaba varios errores, dos de ellos estaban en los print:

En el primer print:

print('Hace un sonido')

Para solucionarlo, hacía falta usar una f-string con self, quedando así:

print(f'{self.especie} Hace un sonido')

En el segundo print:

print('Guau!')

Tenía el mismo error por falta de f-string, y quedó así:

print(f'{self.especie} Guau!')

Por último, se añadió:

if __name__ == "__main__":

Ya que el código original tenía:

p = Perro('canino')
p.hablar

Por lo tanto, al correr el código no salía nada porque no se llamaba el método ni se usaba el bloque principal.

Entonces se arregló el código de esta manera:

if __name__ == "__main__":
    animal = Animal("bulldog")
    animal.hablar()

    animal = Perro("bulldog")
    animal.hablar()

Dándole a la clase Animal una especie y el método hablar, y a la clase Perro (que hereda de Animal) definiendo su propio método hablar.

 
