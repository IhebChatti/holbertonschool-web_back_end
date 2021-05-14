import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  set amount(Amount) {
    this._amount = Amount;
  }

  set currency(Curr) {
    if (Curr instanceof Currency === false) throw new TypeError('currency is not instance of Currency');
    this._currency = Curr;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return conversionRate * amount;
  }
}
