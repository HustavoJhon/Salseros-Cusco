function actualizarResumen() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var resumenSheet = spreadsheet.getSheetByName("RESUMEN");
  
  // Obtén la fecha de hoy
  var fechaHoy = new Date();
  
  // Encuentra la última fila con contenido en la columna B
  var ultimaFila = resumenSheet.getLastRow() + 1;
  
  // Establece la fecha de hoy en la columna B
  resumenSheet.getRange(ultimaFila, 2).setValue(fechaHoy);
  
  // Fórmula en C5
  resumenSheet.getRange(ultimaFila, 3).setFormula("=SUMAR.SI.CONJUNTO(Ingresos!C:C, Ingresos!B:B, " + 
    resumenSheet.getRange(ultimaFila, 2).getA1Notation() + ", Ingresos!F:F, \"prado\")");
  
  // Fórmula en D5
  resumenSheet.getRange(ultimaFila, 4).setFormula("=SUMAR.SI.CONJUNTO(Ingresos!C:C, Ingresos!B:B, " + 
    resumenSheet.getRange(ultimaFila, 2).getA1Notation() + ", Ingresos!F:F, \"fotografia\")");
  
  // Fórmula en E5
  resumenSheet.getRange(ultimaFila, 5).setFormula("=SUM(C" + ultimaFila + ":D" + ultimaFila + ")");
}

function mostrarMensajeBienvenida() {
  var mensaje = "¡Bienvenido a esta hoja de cálculo!"; // Personaliza el mensaje de bienvenida

  // Muestra un cuadro de diálogo de alerta con el mensaje
  SpreadsheetApp.getUi().alert("Mensaje de Bienvenida", mensaje, SpreadsheetApp.getUi().ButtonSet.OK);
}


