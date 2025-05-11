var mysql = require("mysql2/promise");

const db = mysql.createConnection({
  host: "localhost",
  database: "stringify",
  user: "root",
  password: "",
});

const getConnection = async () => await db;

module.exports = {
  getConnection,
};
