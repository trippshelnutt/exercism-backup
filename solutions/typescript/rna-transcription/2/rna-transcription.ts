function dnaToRnaNucleotide(dna: string): string {
  switch(dna) {
    case 'G': return 'C';
    case 'C': return 'G';
    case 'T': return 'A';
    case 'A': return 'U';
  }
  return '';
}
const dnaToRnaMap = new Map<string, string>([
  ['G', 'C'],
  ['C', 'G'],
  ['T', 'A'],
  ['A', 'U'],  
]);

function isValidDna(dna: string): boolean {
  return 'GCTA'.includes(dna);
}

export function toRna(dna: string): string {
  const dnaNucleotides = dna.split('');

  if (!dnaNucleotides.every(isValidDna)) {
    throw new Error("Invalid input DNA.");
  }
  
  return dnaNucleotides.map(d => dnaToRnaMap.get(d)).join('');
}
