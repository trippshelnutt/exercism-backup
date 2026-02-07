export function decodedValue(colors: string[]): number {
  const number1 = colorList.indexOf(colors[0]) * 10;
  const number2 = colorList.indexOf(colors[1]);

  return number1 + number2;
}

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