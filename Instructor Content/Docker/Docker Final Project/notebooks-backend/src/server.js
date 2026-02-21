const express = require("express");
const notebookRouter = require("./routes");

const port = process.env.PORT;
const app = express();
const bodyParser = require("body-parser");

app.use(bodyParser.json());

const mongoose = require("mongoose");

app.get("/api/notebooks/health", (req, res) => {
  res.json({
    message: "hello from notebooks",
  });
});
app.use("/api/notebooks", notebookRouter);


mongoose
  .connect(process.env.DB_URL)
  .then(() => {
    console.log("Connected MongoDB, starting server");
    app.listen(port, () => {
      console.log(`notebooks server listening on port ${port}`);
    });
  })
  .catch((err) => {
    console.error("Something went wrong", err);
  });
