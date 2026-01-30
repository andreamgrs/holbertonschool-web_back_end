export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }

    if (typeof length !== 'number') {
      throw new TypeError('length must be a number');
    }

    if (!Array.isArray(students)) {
      throw new TypeError('students must be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

    get name() {
      return this._name;
    }

    set name(value) {
      this._name = value;
    }

    get length() {
      return this._length;
    }

    set length(value) {
      if (typeof value !== 'number') {
        throw new TypeError('length must be a number');
      }
      this._length = value;
    }

    get students() {
      return this._students;
    }

    set students(value) {
      this._students = value;
    }
}
