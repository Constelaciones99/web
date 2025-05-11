var mysql = require("mysql");

var con = mysql.createConnection({
  host: "localhost",
  database: "stringify",
  user: "root",
  password: "",
});

con.connect(function (error) {
  if (error) {
    throw error;
  } else {
    console.log("CONEXION EXITOSA");
  }
});



con.query("select * from usuario", function (error, resultado) {
  resultado.forEach((element) => {
    console.log(element);
  });
});

con.end();
