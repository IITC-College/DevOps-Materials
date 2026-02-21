const express = require("express");
const Note = require("./models");
const mongoose = require("mongoose");
const axios = require("axios");

const notebooksApiUrl = process.env.NOTEBOOKS_API_URL;
const noteRouter = express.Router();

const validateId = (req, res, next) => {
  const { id } = req.params;

  if (!mongoose.Types.ObjectId.isValid(id)) {
    return res.status(404).json({
      error: "Note not found",
    });
  }

  next();
};

noteRouter.post("/", async (req, res) => {
  try {
    const { title, content, notebookId } = req.body;
    let validatedNotebookId = null;

    if (!notebookId) {
      console.info("Notebook ID not provided. Storing note without notebook.");
    } else if (!mongoose.Types.ObjectId.isValid(notebookId)) {
      return res.status(400).json({
        error: "Notebook not found",
        notebookId,
      });
    } else {
      try {
        await axios.get(`${notebooksApiUrl}/api/notebooks/${notebookId}`);
      } catch (error) {
        const jsonError = error.toJSON();

        if (jsonError.status === 404) {
          return res.status(400).json({
            error: "Notebook not found",
          });
        }

        console.error(
          "Error verifying notebook ID. Upstream service not available. Storing for later validation.",
          {
            notebookId,
            error: error.message,
          }
        );
      } finally {
        validatedNotebookId = notebookId;
      }
    }

    if (!title || !content) {
      return res.status(400).json({
        error: "Title and content fields are required",
      });
    }

    const note = new Note({
      title,
      content,
      notebookId: validatedNotebookId,
    });

    await note.save();

    res.status(201).json({
      data: note,
    });
  } catch (error) {
    res.status(500).json({
      error: error.message,
    });
  }
});

noteRouter.get("/", async (req, res) => {
  try {
    const notes = await Note.find();

    res.json({
      data: notes,
    });
  } catch (error) {
    res.status(500).json({
      error: error.message,
    });
  }
});

noteRouter.get("/:id", validateId, async (req, res) => {
  try {
    const note = await Note.findById(req.params.id);

    if (!note) {
      return res.status(404).json({
        error: "Note not found",
      });
    }

    res.json({ data: note });
  } catch (error) {
    res.status(500).json({
      error: error.message,
    });
  }
});

noteRouter.put("/:id", validateId, async (req, res) => {
  try {
    const { title, content } = req.body;

    const note = await Note.findByIdAndUpdate(
      req.params.id,
      { title, content },
      { new: true },
    );

    if (!note) {
      return res.status(404).json({
        error: "Note not found",
      });
    }

    res.json({ data: note });
  } catch (error) {
    res.status(500).json({
      error: error.message,
    });
  }
});

noteRouter.delete("/:id", validateId, async (req, res) => {
  try {
    const note = await Note.findByIdAndDelete(req.params.id);

    if (!note) {
      return res.status(404).json({
        error: "Note not found",
      });
    }

    res.status(204).send();
  } catch (error) {
    res.status(500).json({
      error: error.message,
    });
  }
});

module.exports = noteRouter;
