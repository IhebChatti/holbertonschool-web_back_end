const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('smoke test', function () {
  it('checks output', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(4.8, 1), 6);
    assert.strictEqual(calculateNumber(5.8, 1.4), 7);
  });
  it('check arguments', function () {
    assert.strictEqual(isNaN(calculateNumber()), true);
  });
  it('check negative args', function () {
    assert.strictEqual(calculateNumber(-2, 4), 2);
    assert.strictEqual(calculateNumber(-5, -10), -15);
  });
});
