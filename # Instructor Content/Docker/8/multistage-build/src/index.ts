import express, { Request, Response } from "express";

const app = express();
const port = process.env.PORT;

app.get("/", (req: Request, res: Response) => {
  res.send("hello from express");
});

app.listen(port, () => {
  console.log(`server listening on ${port}`);
});