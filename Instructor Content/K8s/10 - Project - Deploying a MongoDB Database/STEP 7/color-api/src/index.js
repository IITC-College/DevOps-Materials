const express = require("express");

// Routers
const healthRouter = require("./routes/health");
const apiRouter = require("./routes/api");
const rootRouter = require("./routes/root");

// Utils
const port = 80;
const app = express();

const delayStartup = process.env.DELAY_STARTUP === "true";

console.log(`Delay startup: ${delayStartup}`);

app.use("/api", apiRouter);
app.use("/", healthRouter);
app.use("/", rootRouter);

if (delayStartup) {
  const start = Date.now();
  while (Date.now() - start < 60000) {}
}

app.listen(port, () => {
  console.log(`Color API listening on port: ${port}`);
});