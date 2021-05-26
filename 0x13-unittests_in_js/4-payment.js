const Utils = require('./utils');
module.exports = function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const call = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${call}`);
}
