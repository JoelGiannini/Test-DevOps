# Test-DevOps

Ejercicio 2:

2)	Armar un playbook en Ansible para instalar zabbix-agent2, sabiendo que Zabbix Server esta en 10.0.0.1 y se tiene el servicio de iptables activo.

## Resolucion:

El script se probo en un solo servidor, por esta razon tiene setiado los parametros hosts: localhost y connection: local.
En caso que se quiera probar para una instalacion no local hay que modificar los parametros mencionados anteriormente.

Recomendaciones:
Asegurarse de que en el servividor donde se tenga instalado ansible tenga cruzada las llaves a los equipos a los que se quiera llegar.
Ademas es conveninte agregar los servidores en los cuales se va a trabajar en el archivo /etc/ansible/hosts. En este archivo se puede configurar no solo el parque de servidores sino que se pueden generar grupos de servidores para facilitar la tarea.

* Scripts

[zabbix-agent2.yml](https://github.kyndryl.net/Matias-Joel-Giannini/FREQUENTLY_TASKS/wiki/_Sidebar/_edit)
[habilitar_port.sh](https://docs.github.com/es/communities/documenting-your-project-with-wikis/editing-wiki-content)

