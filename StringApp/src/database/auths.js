const db = require("./connection.js");

async function login(req, res) {}

async function register(req, res) {
  const name = req.body.fullname;
  const nick = req.body.user;
  const clave = req.body.pass;
  //const mail = req.body.email;
  const pais = req.body.country;
  const dat_nick = req.body.ver_nicks;

  var ver_nick = false;

  let dia = new Date();
  var fec_hoy =
    dia.getFullYear() + "/" + dia.getMonth() + 1 + "/" + dia.getDate();

  const connect = await db.getConnection();
  let registrar =
    "INSERT INTO usuario (fullname, user,pass,state, email,date_create,country) VALUES ('" +
    name +
    "','" +
    nick +
    "','" +
    clave +
    "','1','"+
    "','" +
    fec_hoy +
    "','" +
    pais +
    "'  )";

  if (!name || !nick || !clave || !pais) {
    res
      .status(400)
      .send({ status: "Error", message: "LOS CAMPOS ESTAN VACIOS" });
    console.log("falta llenar campos");
    ver_nick = true;
    return;
  } else {
    ver_nick = false;
  }

  dat_nick.forEach(nicky => {
    if (nicky === nick) {
      ver_nick = true;
    }
  });

  if (ver_nick == true) {
    res.status(400).send({ status: "Error", message: " USUARIO YA EXISTENTE" });
    console.log("usuario ya registrado");
    return;
  } else {
    connect.query(registrar);

    console.log("USUARIO REGISTRADO!");
    console.log(req.body);
  }
}

module.exports = { login, register };
