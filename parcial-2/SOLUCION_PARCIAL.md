#Solucion del parcial corte1 
 ##Paso a Paso del ejercicio estructural 
 
 El codigo presentaba un error en su ultimo print el cual era
 **"print(maximo(nums)"**
 El cual para solucionarlo solo era cerrar la instruccion del print ya que solo se tenia la cadena abierta y no se habia cerrado
 para terminar con un print tal que asi:
 **"print(maximo(nums))"**


 ##Paso a paso del ejercicio de oop

 El codigo presentaba varios errores los cuales dos de ellos estaban en los prints:
 **"print('Hace un sonido')"**
 el cual para solucionarlo nos faltaria el f-string y el self, para que quede asi:
 **"print(f'{self.especie} Hace un sonido')"**

 El segundo print tenia el mismo error del f-string, estaba asi:
 **"print( 'Guau !')"**
 Y ahora quedaria asi:
 print(f' {self.especie} Guau!')

 Por ultimo se le añadio un **"if __name__ == "__main__":"**
 ya que se tenia en el codigo lo siguiente:
 **p = Perro('canino')
 p.hablar**
 Por lo tanto a la hora de correr el codigo no salia nada, entonces tambien se hizo un arreglo ahi 
 **if __name__ == "__main__":
  animal = Animal ("bulldog")
  animal.hablar()
  animal = Perro("bulldog")
  animal.hablar()**
 dandole a la clase Animal una especie y el motodo hablar tambien perro heredando de animal y definiendo el metodo de hablar. 

 
