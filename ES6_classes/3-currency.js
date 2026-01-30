export default class Currency {
  constructor(code, name) {
    this._code = code
    this._name = name
  }

  get (code) {
    return this._code
  }
  set (newCode) {
    return this._name = newCode
  }
  get (name) {
    return this._name
  }
  set (newName) {
    return this._name = newName
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}