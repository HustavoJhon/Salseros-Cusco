# table  inactivos
_para registrar a los estudiante en esta tabla se debe tener en cuenta que primero se tiene que buscar por su numero de celular para encontrar una incidencia si el cliente ya fue registrado anteriormente_

### Id
> Nro de registro de todos los estudiantes que se registraron en Inactivos Tipo de dato:_int_
**Formula**
_SI(expresion_logica, valor_si_verdadero,valor_si_falso)_
`=SI(B2<>"",""&FILA()-1, "")`

### Sexo 
> tipo de dato bull (M) masculino (F) femenino.

### Nombre
> nombre del cliente (primer nombre, primer apellido)

### Telefono 
> numero de celular (Whatsapp) de los clientes registrados

### Pago 
> numero decimal con el formato de (sol peruano) 
_Formato > numeoro > Nuevo sol Peruano

### Metodo
> metodo de pago con el que se realizo el pago del cliente (efctivo, yape, plin, transferencia)

### Curso
> curso al cual el cliente se incribio (salsa, bachata, salsa y bachata, coreografia)

### Fecha Inicio
> Fecha de inicio de clases del cliente
_Formato > Numero > Fecha_
`mm/dd/yy` mes/dia/anio 

### Fecha Fin
> Fecha de fin de clases del cliente
_Formato > Numero > Fecha_ 
'mm/dd/yy' mes/dia/anio 

### Meses
> tiempo de incidencia del cliente con el (Nro) de meses que estuboen clases. 
_numero_

### Detalle
> detalle del cliente si es un estudiante (inicial, basico, intermedio, avanzado)

### Clases
> el tipo de clases que tomo el cliente si fue (publica, privada)
_mejora ya que se tiene que cambiar de publica a grupal

### Lugar
> sede del cual se inscribio el cliente 

### Correo
> correo electronico de los clientes

### Descripcion
> descripcion (fechas anteriorores en las que se incribieron los clientes)
