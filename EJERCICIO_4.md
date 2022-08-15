# Test-DevOps

## Ejercicio 4

4)	Se tienen dos instancias de openshift / kubernetes, proponer una solución que realice un balanceo con prioridad en una de las instancias.
-	ocp-instancia-01
-	ocp-instancia-02

### Resolucion

La solicion que yo consideraria seria configurar un servicio de load balance aplicandole la prioridad y preferencia de pods 
creando un objeto de PriorityClass usando priorityClassName en las especificaciones del pod


### Ejemplo de PriorityClass:
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority 
value: 1000000 
preemptionPolicy: PreemptLowerPriority 
globalDefault: false 
description: "This priority class should be used for XYZ service pods only." 

### Procedimiento: 

* Crea una clases prioridad
* Editar los pods existentes para incluir el nombre de PriorityClass

Ejemplo de configuracion de pod con asociado a una PriorityClass:

apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  priorityClassName: high-priority
  
  
