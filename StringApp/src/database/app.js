const express = require("express");
const cors = require("cors");
const db = require("./connection.js");

const methods = require("./auths.js");

const app = express();

app.set("port", 3100);
app.listen(app.get("port"));
console.log("Servidor iniciado en el puerto 3100");

//Middlewares
app.use(
  cors({
    origin: ["http://localhost:3000","http://localhost:3100","http://localhost:3300","http://localhost:8080", "http://127.0.0.1", "http://localhost"],
  })
);

//Configuration
app.use(express.json())

//RUTAS
app.post("/api/register",methods.register)
app.post("/api/login",methods.login)


app.get("/api/datos", async (req, res) => {
  const connect = await db.getConnection();
  const result = await connect.query("SELECT * FROM usuario");
  res.json(result);
});
