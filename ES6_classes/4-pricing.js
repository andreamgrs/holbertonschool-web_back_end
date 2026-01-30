import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a Currency instance');
    }

    this._amount = amount;
    this._currency = currency;
  }

  get amount() { return this._amount; }

  set code(newAmount) {
    this._amount = newAmount;
  }

  get currency() { return this._currency; }

  set name(newCurrency) {
    this._currency = newCurrency;
  }

  displayFullPrice() {
    return `${this._amount} ${this.currency._name} (${this.currency._code})`;
  }

  static convertPrice(amount, conversionRate){
    return amount * conversionRate;
  }
}