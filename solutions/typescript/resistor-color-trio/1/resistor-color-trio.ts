export function decodedResistorValue(colors: string[]) {
  const [first, second, third] = colors;
  
  const firstValue = colorList.indexOf(first) * 10;
  const secondValue = colorList.indexOf(second);

  const value = firstValue + secondValue;

  const thirdValue = colorList.indexOf(third);
  const power = 10 ** thirdValue;

  const valueWithPower = value * power;

  if (valueWithPower > giga) {
    return `${valueWithPower / giga} gigaohms`;
  }
  if (valueWithPower > mega) {
    return `${valueWithPower / mega} megaohms`;
  }
  if (valueWithPower > kilo) {
    return `${valueWithPower / kilo} kiloohms`;
  }

  return `${valueWithPower} ohms`;
}

const giga: number = 10**9;
const mega: number = 10**6;
const kilo: number = 10**3;

const colorList: string[] = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white' 
];