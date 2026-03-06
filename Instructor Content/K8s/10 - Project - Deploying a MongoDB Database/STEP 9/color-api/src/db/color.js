const mongoose = require("mongoose");

const ColorSchema = new mongoose.Schema({
  key: String,
  value: String,
});

const Color = mongoose.model("Color", ColorSchema);

const saveColor = async ({ key, value }) => {
  let color = await Color.findOne({ key });

  if (color) {
    color.set({ value });
  } else {
    color = new Color({ key, value });
  }

  await color.save();
};

const getColors = async () => {
  const colors = await Color.find();
  return colors;
};

const getColor = async ({ key, strict = false }) => {
  let color = await Color.findOne({ key });

  if (strict && !color) {
    return undefined;
  }
  if (color) {
    return color.value;
  }

  return process.env.DEFAULT_COLOR || "black";
};

const deleteColor = async (key) => {
  await Color.deleteOne({ key });
};

module.exports = { saveColor, getColors, getColor, deleteColor };
