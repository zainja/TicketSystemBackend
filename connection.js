// imports
const mysql = require('mysql')
require('dotenv').config()
mysqlInfo = {
    host: 34.89.204.130,
    user: root,
    password: OjDdwiJoHDrjHiAC,
    database: ticket
}
// connection set up
const connection = mysql.createConnection(mysqlInfo)
connection.connect()
module.exports = connection
