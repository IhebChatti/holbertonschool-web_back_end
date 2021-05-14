export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  set code(Code) {
    this._code = Code;
  }

  set name(Name) {
    this._name = Name;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
