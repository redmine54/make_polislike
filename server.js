// server.js
/*
Expressを使用して、フロントエンドの静的ファイルを提供するサーバーを作成します。
$ npm init -y
$ npm install express
*/
/*
起動：
  node server.js &
停止
  kill $(lsof -t -i:8880)
*/
const express = require("express");
const app = express();
const path = require("path");

app.use(express.static(path.join(__dirname, "frontend")));

app.listen(8880, () => {
  console.log("Frontend running at http://localhost:8880");
});
