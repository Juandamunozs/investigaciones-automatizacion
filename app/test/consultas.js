// // Boton de antecedentes judiciales
// respuesta = document.getElementsByClassName("ui-button-text ui-c");
// if (respuesta) {
//   respuesta[0].click();
// }

// //TODO: PROCESOS DE LA RAMA JUDICIAL
// // Todos los procesos de la rama judicial
// todoProcesos = document.evaluate(
//   "/html/body/div[1]/div/div[3]/main/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div",
//   document,
//   null,
//   XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
//   null
// );

// if (todoProcesos.snapshotLength > 0) {
//   todoProcesos.snapshotItem(0).click();
// }

// // sppiner
// persona_natural = document.getElementById("input-72");

// if (persona_natural) {
//   persona_natural.click();
//   console.log("Persona natural seleccionada");
// } else {
//   console.log("No se encontró el elemento persona natural");
// }

// // Persona natural

// tipo_persona = document.evaluate(
//   "/html/body/div[1]/div[2]/div/div[1]/div/div",
//   document,
//   null,
//   XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
//   null
// );

// console.log(tipo_persona);

// if (tipo_persona.snapshotLength > 0) {
//   tipo_persona.snapshotItem(0).click();
//   console.log("Tipo de persona seleccionado");
// } else {
//   console.log("No se encontró el tipo de persona");
// }

// // Ingresar el nombre de la persona a consultar

// input_nombre = document.getElementById("input-78");

// if (input_nombre) {
//   input_nombre.click();

//   input_nombre.focus();

//   input_nombre.value = "25485789";

//   input_nombre.dispatchEvent(new Event("input"));

//   console.log("Valor insertado correctamente");
// }

// //script py
// // script = f"""document.getElementById('txtNumDoc').value = '{documento}';"""
// //         driver.execute_script(script)

// // click en consultar

// boton_consultar = document.getElementsByClassName(
//   "v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--default success mt-2 mx-2 font-weight-bold"
// );

// if (boton_consultar.length > 0) {
//   boton_consultar[0].click();
//   console.log("Botón clickeado");
// }

// //Extraer la información de la consulta

// // Obtener todos los elementos con la clase 'pl-1'
// let respuesta = document.getElementsByClassName("pl-1");

// if (respuesta.length > 0) {
//   console.log(respuesta[0].textContent);
//   return respuesta[0].textContent;
// } else {
//   console.log('No se encontraron elementos con la clase "pl-1"');
//   return null;
// }

// //TODO: PROCESOS DE LA RAMA JUDICIAL de la tabla
// for (let tabla of tablas) {
//   let filas = tabla.getElementsByTagName("tr");
//   let tablaContenido = [];

//   for (let fila of filas) {
//     let celdas = fila.getElementsByTagName("td");
//     let filaContenido = [];

//     for (let celda of celdas) {
//       filaContenido.push(celda.textContent.trim());
//     }

//     if (filaContenido.length > 0) {
//       tablaContenido.push(filaContenido);
//     }
//   }

//   if (tablaContenido.length > 0) {
//     contenidoTablas.push(tablaContenido);
//   }
// }

// return contenidoTablas;

// //Verficar check antecendntes policiales

// // Seleccionamos el checkbox del reCAPTCHA
// let captchaCheckbox = document.querySelector(".recaptcha-checkbox");

// // Verificamos si el reCAPTCHA ya está marcado
// let isChecked = captchaCheckbox.getAttribute("aria-checked");

// if (isChecked === "false") {
//   console.log("reCAPTCHA no está marcado. Haciendo clic para marcarlo...");
//   return false;
// } else {
//   console.log("reCAPTCHA ya está marcado automaticamente. Continuando...");
//   return true;
// }

// // Extarer resultados de la consulta de funcion publica

// respuesta = document.getElementsByClassName("odd");

// if (respuesta.length > 0) {
//   console.log(respuesta[0].textContent);
// } else {
    
//   respuesta = document.getElementById("div-resultados-busqueda");

//   if (respuesta) {
//     console.log(respuesta.textContent);
//   } else {
//     console.log("No se encontraron resultados");
//   }
// }

// // input con js
// try {
//   // Seleccionar el campo de texto usando el ID
//   let inputDocumento = document.getElementById('txtNumID');
  
//   // Verificar si el campo existe antes de asignar el valor
//   if (inputDocumento) {
//       inputDocumento.value = "123456789"; // Reemplaza con el valor que deseas insertar
//   } else {
//       console.log("Campo no encontrado");
//   }
// } catch (e) {
//   console.log(`Reintentando ingreso de documento: ${e}`);
// }
