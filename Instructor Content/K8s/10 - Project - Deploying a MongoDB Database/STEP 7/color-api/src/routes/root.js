const rootRouter = require("express").Router();
const { getHostname } = require("../utils.js");
const { getColors } = require("../db/color.js");

rootRouter.get("/", (req, res) => {
  const { colorKey } = req.query;

  console.log(`Received request for colorKey: ${colorKey}`);
  const hostname = getHostname();
  const color = getColors({ key: colorKey });

  res.send(
    `<h1 style="color:${color};">Hello from Color API</h1> 
    <h2>Hostname: ${hostname}</h2>`,
  );
});

module.exports = rootRouter;