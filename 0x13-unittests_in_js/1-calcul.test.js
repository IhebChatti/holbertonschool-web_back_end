const calculateNumber = require('./1-calcul.js');
const assert = require('assert');

describe('smoke test', function () {
  it('checks output for SUM', function () {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    assert.strictEqual(calculateNumber('SUM', 2, 5.6), 8);
    assert.strictEqual(calculateNumber('SUM', 3.5, 2.7), 7);
    assert.strictEqual(calculateNumber('SUM', 3, 2.5), 6);
  });
  it('check output for SUBTRACT', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.strictEqual(calculateNumber('SUBTRACT', 2, 1.1), 1);
    assert.strictEqual(calculateNumber('SUBTRACT', 7.2, 5), 2);
  });
  it('check output for DIVIDE', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.strictEqual(calculateNumber('DIVIDE', -5, 2), -2.5);
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
