const express = require("express");

// Utils
const { getHostname } = require("../utils.js");
const {
  getColors,
  getColor,
  deleteColor,
  saveColor,
} = require("../db/color.js");
const apiRouter = express.Router();

apiRouter.get("/", async (req, res) => {
  const { format, colorKey } = req.query;

  console.log(`Received request for colorKey: ${colorKey}`);

  const color = await getColor({ key: colorKey });
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

apiRouter.get("/color", async (req, res) => {
  const colors = await getColors();
  res.send({ data: colors });
});

apiRouter.get("/color/:key", async (req, res) => {
  const { key } = req.params;

  const color = await getColor({ key, strict: true });

  if (!color) {
    return res.status(404).send({ error: "Color not found" });
  } else {
    return res.send({ data: color });
  }
});

apiRouter.post("/color/:key", async (req, res) => {
  const { key } = req.params;
  const { value } = req.body;

  await saveColor({ key, value });

  return res.status(201).send({ message: "Color updated successfully" });
});

// apiRouter.put("/color/:key", async (req, res) => {
//   const { key } = req.params;
//   const { value } = req.body;

//   await saveColor({ key, value });

//   return res.status(200).send({ message: "Color updated successfully" });
// });

apiRouter.delete("/color/:key", async (req, res) => {
  const { key } = req.params;
  await deleteColor(key);
  res.status(204).send(
    "Color deleted successfully"
  );
});

module.exports = apiRouter;
