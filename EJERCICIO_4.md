# Test-DevOps

## Ejercicio 4

4)	Se tienen dos instancias de openshift / kubernetes, proponer una solución que realice un balanceo con prioridad en una de las instancias.
-	ocp-instancia-01
-	ocp-instancia-02

### Resolución

La solución sería configurar un servicio de load-balance aplicándole la prioridad y preferencia de pods 
creando un objeto de PriorityClass usando priorityClassName en las especificaciones del pod


### Ejemplo de PriorityClass:

 <img width="659" alt="Captura de Pantalla 2022-08-15 a la(s) 19 53 26" src="https://user-images.githubusercontent.com/111232232/184734291-2dcdbb4e-608e-4b77-9de8-fcfa976649b1.png">

### Procedimiento: 

* Crea una PriorityClass
* Editar los pods existentes para incluir el nombre de PriorityClass

Ejemplo de configuración de pod asociado a una PriorityClass:

<img width="316" alt="Captura de Pantalla 2022-08-15 a la(s) 19 52 56" src="https://user-images.githubusercontent.com/111232232/184734377-33a846e8-4fcc-4a22-8822-3ab9ce40af26.png">

  
 

