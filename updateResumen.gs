function myFunction() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  // Insert a new row at row 5
  sheet.insertRowBefore(5);

  // Set the value in cell B5 to today's date
  sheet.getRange("B5").setValue(new Date());

  // Calculate SUMIFS for cell C6
  var ingresosSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Ingresos");
  var c6Value = 0;
  var limacpampa = "limacpampa";
  for (var i = 1; i <= ingresosSheet.getLastRow(); i++) {
    var cellValue = ingresosSheet.getRange(i, 1).getValue(); // Assuming column 1 contains the criteria
    if (cellValue === limacpampa) {
      var criteria1 = ingresosSheet.getRange(i, 2).getValue(); // Assuming column 2 contains the first criteria
      var criteria2 = ingresosSheet.getRange(i, 4).getValue(); // Assuming column 4 contains the second criteria
      c6Value += criteria1 * criteria2;
    }
  }
  sheet.getRange("C6").setValue(c6Value);

  // Calculate SUMIFS for cell C5
  var c5Value = 0;
  for (var j = 1; j <= ingresosSheet.getLastRow(); j++) {
    var cellValue = ingresosSheet.getRange(j, 1).getValue(); // Assuming column 1 contains the criteria
    if (cellValue === limacpampa) {
      var criteria1 = ingresosSheet.getRange(j, 2).getValue(); // Assuming column 2 contains the first criteria
      var criteria2 = ingresosSheet.getRange(j, 3).getValue(); // Assuming column 3 contains the second criteria
      c5Value += criteria1 * criteria2;
    }
  }
  sheet.getRange("C5").setValue(c5Value);

  // Set the value in cell D6 to the value in D5
  var d5Value = sheet.getRange("D5").getValue();
  sheet.getRange("D6").setValue(d5Value);

  // Clear the values in column D
  sheet.getRange("D:D").clearContent();

  // Calculate SUMIFS for cell D5
  var prado = "prado";
  var d5ValueNew = 0;
  for (var k = 1; k <= ingresosSheet.getLastRow(); k++) {
    var criteria1 = ingresosSheet.getRange(k, 1).getValue(); // Assuming column 1 contains the criteria
    if (criteria1 === prado) {
      var criteria2 = ingresosSheet.getRange(k, 2).getValue(); // Assuming column 2 contains the first criteria
      d5ValueNew += criteria2;
    }
  }
  sheet.getRange("D5").setValue(d5ValueNew);

  // Calculate SUMIFS for cell E5
  var fotografia = "fotografia";
  var e5Value = 0;
  for (var l = 1; l <= ingresosSheet.getLastRow(); l++) {
    var criteria1 = ingresosSheet.getRange(l, 2).getValue(); // Assuming column 2 contains the criteria
    if (criteria1 === fotografia) {
      var criteria2 = ingresosSheet.getRange(l, 3).getValue(); // Assuming column 3 contains the criteria
      e5Value += criteria2;
    }
  }
  sheet.getRange("E5").setValue(e5Value);

  // Calculate the sum of C5, C6, and D5 and set it in F5
  var f5Value = c5Value + c6Value + d5ValueNew;
  sheet.getRange("F5").setValue(f5Value);

  // Clear the value in F6
  sheet.getRange("F6").clearContent();
}

