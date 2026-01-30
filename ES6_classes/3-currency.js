export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new TypeError('code must be a string');
    }

    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }

    this._code = code
    this._name = name
  }

  get (code) {
    return this._code
  }
  set (newCode) {
    return this._code = newCode
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