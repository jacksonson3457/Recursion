const net = require("net");

const request = JSON.stringify({
  jsonrpc: "2.0",
  method: "floor",
  params: [2.5],
  id: 1,
});

//サーバーへの接続設定
const client = net.createConnection({ path: "/tmp/socket_file" }, () => {
  console.log("Connected to Server");
  client.write(request);
});

client.on("data", (data) => {
  const response = JSON.parse(data);
  console.log("Received: " + response.result);
  client.end();
});

client.on("error", (err) => {
  console.log("Connention Error: " + err.message);
});
