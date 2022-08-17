# Test-DevOps

## Ejercicio 7

7)	Automatizar un proceso el cual se conecta a servidores linux y verifica cuantos CLOSE_WAIT existen en el servidor hacia la direccion 8.8.8.8:443

### Resolucion

Este script se  ejectuto ejecuto sin el filtro por la ip 8.8.8.8:443 debido a que en la los servidores que utilice de prueba no tenian nada en estado CLOSE_WAIT
con esa ip en cuestion.
Igualmente se dejo preparado para que filtre por la ip 8.8.8.8:443 con otra linea comentada para que valide solo las conecciones en CLOSE_WAIT.

## Scripts

[close_wait_verif.sh](https://github.com/JoelGiannini/Test-DevOps/blob/main/close_wait_verif.sh)

## Salida

[close_wait.log](https://github.com/JoelGiannini/Test-DevOps/blob/main/close_wait.log)

### Detalles a tener en cuenta: 
El script se probo en un servidor satellite que esta configurado para que un deterimnado usuario pueda acceder a los servidores con root en caso 
de que se quiera probar la corrida dependiendo de como este configurado el acceso a los servidores se debera agregar el usuario que tenga acceso a los equipos.
ejemplo la coneccion ssh se realizo "ssh -q $i" donde i es la variable de servidor, en caso de requerir un usuario especifico deberia quedar "ssh -q user@$i".

### Se detallan unos print de pantalla con la corrida del script:


<img width="923" alt="Captura de Pantalla 2022-08-15 a la(s) 13 36 56" src="https://user-images.githubusercontent.com/111232232/184677098-86ee6368-024a-4125-9a85-46d2e410c4c8.png">
<img width="552" alt="Captura de Pantalla 2022-08-14 a la(s) 20 20 10" src="https://user-images.githubusercontent.com/111232232/184676427-f9ec181d-90f5-4899-9ca8-34b07e0d74d5.png">
<img width="428" alt="Captura de Pantalla 2022-08-14 a la(s) 20 22 19" src="https://user-images.githubusercontent.com/111232232/184676441-d67e300a-10f8-4edf-948d-278a39ef76cb.png">
<img width="480" alt="Captura de Pantalla 2022-08-14 a la(s) 20 24 14" src="https://user-images.githubusercontent.com/111232232/184676447-83eb8546-0227-4808-82f4-a8959876dadd.png">
