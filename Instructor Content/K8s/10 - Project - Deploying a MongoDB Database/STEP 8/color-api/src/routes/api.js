const express = require("express")

// Utils
const { getHostname} = require("../utils.js");
const { getColors } = require("../db/color.js");

const apiRouter = express.Router()

apiRouter.get("/", async (req, res) => {
  const { format, colorKey } = req.query; 

    console.log(`Received request for colorKey: ${colorKey}`);

  const color = await getColors({ key: colorKey });
  const hostname = getHostname();

  if (format === "json") {
    return res.json({
      color,
      hostname,
    });
  } else {
    return res.send(`COLOR: ${color}, HOSTNAME: ${hostname}`);
  }
}); 

module.exports = apiRouter