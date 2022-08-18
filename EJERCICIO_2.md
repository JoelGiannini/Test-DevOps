# Test-DevOps

Ejercicio 2:

2)	Armar un playbook en Ansible para instalar zabbix-agent2, sabiendo que Zabbix Server esta en 10.0.0.1 y se tiene el servicio de iptables activo.

## Resolucion:

El script se probo en una instalación local y teniendo en cuenta que el Zabbix server es 44.201.81.17 (en el script se apunta a 10.0.0.1 como pide el ejercicio), por esta razon tiene setiado los parametros hosts: localhost y connection: local.
En caso que se quiera probar para una instalacion no local hay que modificar los parametros mencionados anteriormente.

Recomendaciones:
Asegurarse de que en el servividor donde se tenga instalado ansible tenga cruzada las llaves a los equipos a los que se quiera llegar.
Ademas es conveninte agregar los servidores en los cuales se va a trabajar en el archivo /etc/ansible/hosts. En este archivo se puede configurar no solo el parque de servidores sino que se pueden generar grupos de servidores para facilitar la tarea.

### Scripts

[zabbix-agent2.yml](https://github.com/JoelGiannini/Test-DevOps/blob/main/zabbix-agent2.yml)

[habilitar_port.sh](https://github.com/JoelGiannini/Test-DevOps/blob/main/habilitar_port.sh)

### Prints de pantallas

<img width="1116" alt="Captura de Pantalla 2022-08-18 a la(s) 01 03 42" src="https://user-images.githubusercontent.com/111232232/185292033-2c888d91-74a3-462b-b366-6dc63b6472da.png">

<img width="598" alt="Captura de Pantalla 2022-08-18 a la(s) 01 05 34" src="https://user-images.githubusercontent.com/111232232/185292058-2d64f1c0-5af2-4873-bdfe-02a88515a374.png">

<img width="875" alt="Captura de Pantalla 2022-08-18 a la(s) 01 09 11" src="https://user-images.githubusercontent.com/111232232/185292082-0ee53c00-75d2-4dac-a17f-3b27ce8e6a16.png">

