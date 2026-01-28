export default function appendToEachArrayValue(array, appendString) {
  let idx = 0
  for (let value in array) {
    value = array[idx];
    array[idx] = appendString + value;
    idx++
  }

  return array;
}