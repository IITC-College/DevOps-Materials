const express = require("express");
const bodyParser = require("body-parser")
const mongoose = require("mongoose");
// Routers
const healthRouter = require("./routes/health");
const apiRouter = require("./routes/api");
const rootRouter = require("./routes/root");

// Utils
const port = 80;
const app = express();

app.use(bodyParser.json());
const delayStartup = process.env.DELAY_STARTUP === "true";

console.log(`Delay startup: ${delayStartup}`);

app.use("/api", apiRouter);
app.use("/", healthRouter);
app.use("/", rootRouter);

if (delayStartup) {
  const start = Date.now();
  while (Date.now() - start < 60000) {}
}
mongoose.connect(process.env.DB_URL).then(() => {
  console.log("Connected to MongoDB");

  app.listen(port, () => {
    console.log(`Color API listening on port: ${port}`);
  });
}).catch((err) => {
  console.error("Failed to connect to MongoDB");
  console.log("================================");
  console.error(err);
  console.log("================================");

});