## Test-DevOps

# Este repositorio contiene un test para medir los conocimientos integrales de DevOps

1)	Dada una aplicación instanciada en 100 servidores que dejan los logs en /var/log/app.log, proponer una solución para centralizar dichos logs en un servidor(s).
-	Describir la solución técnica elegida.
-	Describir en términos técnicos, los cambios a realizar en los servidores de la aplicación como en el servidor que va ser concentrador de los eventos. Y pensando que esta tarea tiene que ser automatizada.


2)	Armar un playbook en Ansible para instalar zabbix-agent2, sabiendo que Zabbix Server esta en 10.0.0.1 y se tiene el servicio de iptables activo.


3)	Describir los controles a nivel de monitoreo que deberían realizarse a un cluster Openshift/Kubernetes, enfocado a los componentes core que hacen que el cluster esté Ready.


4)	Se tienen dos instancias de openshift / kubernetes, proponer una solución que realice un balanceo con prioridad en una de las instancias.
-	ocp-instancia-01
-	ocp-instancia-02


5)	Se necesita disponibilizar un file el cual se tiene que poder consultar vía protocolo http.
URL: https://example.com/file.txt.
Considerando que es para un cluster Openshift o Kubernetes:
-	Armar la imagen docker, lo más mínima posible.
-	Armar los manifiestos necesarios para disponibilizar el endpoint.


6)	Realizar dos script en python para consultar la api de GitHub:
1.	Listar los repositorios de un “usuario” en GitHub
2.	Elegir un repositorio de este usuario y exportar los tags en formato csv con los datos Nombre y Commit


7)	Automatizar un proceso el cual se conecta a servidores linux y verifica cuantos CLOSE_WAIT existen en el servidor hacia un la direccion 8.8.8.8:443
