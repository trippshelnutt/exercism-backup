function dnaToRna(dna: string): string {
  switch(dna) {
    case 'G': return 'C';
    case 'C': return 'G';
    case 'T': return 'A';
    case 'A': return 'U';
  }
  throw new Error("Invalid input DNA.");
}

export function toRna(dna: string): string {
  return [...dna].map(dnaToRna).join('');
}
