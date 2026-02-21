const express = require("express");

const notebookRouter = express.Router();

notebookRouter.get("/", (req, res) => {
  res.json({
    message: "hello from notebooks",
  });
});

module.exports = notebookRouter;