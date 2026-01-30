export default class Car {
  constructor(_brand, _motor, color) {
    this.__brand = _brand;
    this.__motor = _motor;
    this._color = color;
  }
  cloneCar(){
    return new this.constructor();
  }

}