const express = require("express")

const healthRouter = express.Router()

const failLiveness = process.env.FAIL_LIVENESS === "true";
const failReadiness = process.env.FAIL_READINESS === "true" ? Math.random() < 0.5 : false;

console.log(`Fail liveness: ${failLiveness}`);
console.log(`Fail readiness: ${failReadiness}`);

healthRouter.get("/ready", (req, res) => {
  if (failReadiness) {
    return res.sendStatus(503);
  }
  res.send("Ok");
});

healthRouter.get("/up", (req, res) => {
  res.send("Ok");
});

healthRouter.get("/health", (req, res) => {
  if (failLiveness) {
    return res.sendStatus(503);
  }
  res.send("Ok");
});


module.exports = healthRouter