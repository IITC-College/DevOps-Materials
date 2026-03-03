const express = require("express");
const os = require("os");
const fs = require("fs");
const path = require("path");

const getColor = () => {
  let color = process.env.DEFAULT_COLOR;
  const filePath = process.env.COLOR_CONFIG_PATH;

  if (filePath) {
    try {
      const colorFromFile = fs.readFileSync(
        path.resolve(filePath),
        "utf8"
      );

      color = colorFromFile.trim();
    } catch (error) {
      console.error(`Failed to read contents of ${filePath}`);
      console.error(error);
    }
  }

  return color || "blue";
};

const port = 80;
const app = express();
const color = getColor();
const hostname = os.hostname();

const delayStartup = process.env.DELAY_STARTUP === "true";
const failLiveness = process.env.FAIL_LIVENESS === "true";
const failReadiness =
  process.env.FAIL_READINESS === "true" ? Math.random() < 0.5 : false;

console.log(`Delay startup: ${delayStartup}`);
console.log(`Fail liveness: ${failLiveness}`);
console.log(`Fail readiness: ${failReadiness}`);

app.get("/", (req, res) => {
  res.send(
    `<h1 style="color:${color};">Hello from Color API</h1> 
    <h2>${hostname}</h2>`,
  );
});

app.get("/api", (req, res) => {
  const { format } = req.query; // localhost/api?format=text
  if (format === "json") {
    return res.json({
      color,
      hostname,
    });
  } else {
    return res.send(`COLOR: ${color}, HOSTNAME: ${hostname}`);
  }
});

app.get("/ready", (req, res) => {
  if (failReadiness) {
    return res.sendStatus(503);
  }
  res.send("Ok");
});

app.get("/up", (req, res) => {
  res.send("Ok");
});

app.get("/health", (req, res) => {
  if (failLiveness) {
    return res.sendStatus(503);
  }
  res.send("Ok");
});

if (delayStartup) {
  const start = Date.now();

  // Purposefully block the event loop for 60 seconds to simulate a slow startup
  while (Date.now() - start < 60000) {}
}

app.listen(port, () => {
  console.log(`Color API listening on port: ${port}`);
});
