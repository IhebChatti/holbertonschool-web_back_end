const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const chai = require('chai');

describe('smoke test', function () {
  let log;
  beforeEach(function () {
    log = sinon.spy(console, 'log');
  });
  afterEach(function () {
    log.restore();
  });
  it('checks output and number of calls', function () {
    sendPaymentRequestToApi(100, 20);
    chai.expect(log.calledOnce).to.equal(true);
    chai.expect(log.calledWith('The total is: 120')).to.equal(true);
  });
  it('checks output and number of calls', function () {
    sendPaymentRequestToApi(10, 10);
    chai.expect(log.calledOnce).to.equal(true);
    chai.expect(log.calledWith('The total is: 20')).to.equal(true);
  });
});
