const mongoose = require("mongoose")

const ColorSchema = new mongoose.Schema({
  key: String,
  value: String
})

const Color = mongoose.model("Color", colorSchema)

const saveColor = async (key, value) => {

  let color = await Color.findOne({ key })

  if (color) {
    color.set({ value })
  } else {
    color = new Color({ key, value })
  }

  await color.save()
}

const getColors = async () => {
    const colors = await Color.find()
    return colors
}


const getColor = async (key) => {
    let color = await Color.findOne({ key })

    if (color) {
        return color = color.value
    } else {
        return color = process.env.COLOR || "black"
    }
}

module.exports = { saveColor, getColors, getColor }