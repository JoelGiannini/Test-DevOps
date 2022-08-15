# Test-DevOps


 1)	Dada una aplicación instanciada en 100 servidores que dejan los logs en /var/log/app.log, proponer una solución para centralizar dichos logs en un servidor(s).
-	Describir la solución técnica elegida.
-	Describir en términos técnicos, los cambios a realizar en los servidores de la aplicación como en el servidor que va ser concentrador de los eventos. Y pensando que esta tarea tiene que ser automatizada.

### Resolucion:

  La solución más optima es Filebeat + ELK.
Básicamente seria instalar Filebeat en los servidores de la aplicación y configurarle los logs que queramos recolectar y el output al servidor elasticsearch en el archivo filebeat.yml.
Luego Logstash recolecta los logs de diferentes filebeat y los manda al elasticsearch.
Esto lo podemos configurar en el archivo logstash.conf.
Dentro de este archivo podemos configurar el input para que escuche por un puerto al filebeat, el tipo de mensaje y aplicar un filtro si quisiéramos. Además, también tenemos que configurar el output a elasticsearch.
Luego elasticsearch almacena todos los logs que configuramos previamente. 
Por último, Kibana es la interfaz de usuario de elasticsearch; en el dashboard podemos visualizar todos los logs centralizados y formateados.
Mediante esta solución se nos felicita las automatizaciones a futuro.

