const calculateNumber = require('./2-calcul_chai.js');
const chai = require('chai');

describe('smoke test', function () {
  it('checks output for SUM', function () {
    chai.expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    chai.expect(calculateNumber('SUM', 2, 5.6)).to.equal(8);
    chai.expect(calculateNumber('SUM', 3.5, 2.7)).to.equal(7);
    chai.expect(calculateNumber('SUM', 3, 2.5)).to.equal(6);
  });
  it('check output for SUBTRACT', function () {
    chai.expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    chai.expect(calculateNumber('SUBTRACT', 2, 1.1)).to.equal(1);
    chai.expect(calculateNumber('SUBTRACT', 7.2, 5)).to.equal(2);
  });
  it('check output for DIVIDE', function () {
    chai.expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    chai.expect(calculateNumber('DIVIDE', -5, 2)).to.equal(-2.5);
    chai.expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
});
