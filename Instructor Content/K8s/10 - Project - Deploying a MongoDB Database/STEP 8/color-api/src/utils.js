const os = require("os");

const getHostname = () => {
  return os.hostname();
}

module.exports = {
  getHostname,
};