using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

//AUG                   Methionine
//UUU, UUC              Phenylalanine
//UUA, UUG              Leucine
//UCU, UCC, UCA, UCG    Serine
//UAU, UAC              Tyrosine
//UGU, UGC              Cysteine
//UGG                   Tryptophan
//UAA, UAG, UGA         STOP

public static class ProteinTranslation
{
    private static Dictionary<string, string> codonProteinMap = new Dictionary<string, string>
    {
        { "AUG", "Methionine" },
        { "UUU", "Phenylalanine" },
        { "UUC", "Phenylalanine" },
        { "UUA", "Leucine" },
        { "UUG", "Leucine" },
        { "UCU", "Serine" },
        { "UCC", "Serine" },
        { "UCA", "Serine" },
        { "UCG", "Serine" },
        { "UAU", "Tyrosine" },
        { "UAC", "Tyrosine" },
        { "UGU", "Cysteine" },
        { "UGC", "Cysteine" },
        { "UGG", "Tryptophan" },
        { "UAA", "STOP" },
        { "UAG", "STOP" },
        { "UGA", "STOP" },
    };

    public static string[] Proteins(string strand)
    {
        return Enumerable.Range(0, strand.Length / 3)
            .Select(i => strand.Substring(i * 3, 3))
            .Select(c => codonProteinMap[c])
            .TakeWhile(p => p != "STOP")
            .ToArray();
    }
}