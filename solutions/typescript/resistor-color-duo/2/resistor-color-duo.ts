export function decodedValue(colors: string[]): number {
  return colors
    .slice(0, 2)
    .map(getNumber)
    .reverse()
    .reduce(addBands, 0);
}

function getNumber(color: string): number {
  return colorList.indexOf(color);
}

function addBands(acc: number, curr: number, ind: number): number {
  return acc + (curr * 10 ** ind);
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