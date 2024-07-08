# ejercicio_examen



Examen de Desarrollo en Python para Gestión de Créditos Estudiantiles en
AWS


Una institución educativa desea implementar un sistema prototipo para la gestión
de créditos aleatorios para sus estudiantes utilizando Amazon Web Services (AWS).
Este sistema debe simular la asignación de créditos a través de la infraestructura
de AWS, mostrar estadísticas básicas y generar un reporte en formato CSV. El
objetivo es que los estudiantes comprendan los conceptos básicos de la nube y
cómo se pueden aplicar en la gestión de datos y recursos.
alumnos = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro
Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco
Díaz", "Elena Fernández"]
Requerimientos del Sistema:
1. Simulación de Créditos en AWS:
o Utiliza la infraestructura de AWS para simular la asignación de
créditos aleatorios entre $50 y $200 a cada alumno registrado. No es
necesario utilizar Boto3 o servicios específicos de AWS;
simplemente simula este proceso dentro del contexto de un entorno
cloud.


3. Clasificación de Créditos:
o Desarrolla una función que clasifique los créditos de los estudiantes
en los siguientes rangos:
▪ Créditos menores a $100
▪ Créditos entre $100 y $150
▪ Créditos mayores a $150
o Muestra la cantidad de estudiantes en cada rango y sus detalles.


5. Cálculo de Estadísticas de Créditos:
o Implementa una función para calcular las siguientes estadísticas
básicas de los créditos de los estudiantes:
▪ Máximo crédito
▪ Mínimo crédito
▪ Promedio de créditos
6. Generación de Reporte de Créditos:
o Crea una función para generar un reporte en formato CSV que liste
el nombre de cada alumno y su respectivo crédito, además de su
clasificación según los rangos especificados. El archivo debe
denominarse reporte_creditos.csv.


8. Salir del Programa:
o Proporciona una opción para salir del programa cuando el usuario lo
desee.
Consideraciones Adicionales:
• Asegúrate de manejar adecuadamente errores y excepciones que puedan
surgir durante la ejecución del programa.




