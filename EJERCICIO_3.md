# Test-DevOps

Ejercicio 3:

3)	Describir los controles a nivel de monitoreo que deberían realizarse a un cluster Openshift/Kubernetes, enfocado a los componentes core que hacen que el cluster esté Ready.

## Resolucion

### Los controles de monitoreo que deberían realizarse para evitar que en nodo entre en estado not ready son los siguientes:

* Espacio en disco en los nodos Masters y Workers
* Uso de memoria en los nodos Masters y Workers
* Cantidad de procesos ejecutándose en los nodos Masters y Workers
* Conectividad de red del  los nodos  Masters y Workers
* Monitorear que es este ejecutando el kube-proxy
* Monitorear si el kubelet se bloquea o se detiene, para evitar perdida de comunicación con el API server


