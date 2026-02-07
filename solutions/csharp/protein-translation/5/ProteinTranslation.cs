using System;
using System.Collections.Generic;
using System.Linq;

public static class ProteinTranslation
{
    public static string[] Proteins(string strand) =>
        strand
            .ToCodons()
            .Select(ToProtein)
            .TakeWhile(p => p != "STOP")
            .ToArray();

    private static IEnumerable<string> ToCodons(this string strand) =>
        Enumerable.Range(0, strand.Length / 3)
            .Select(i => strand.Substring(i * 3, 3));

    private static string ToProtein(string codon) =>
        codon switch
        {
            "AUG" => "Methionine",
            "UUU" or "UUC" => "Phenylalanine",
            "UUA" or "UUG" => "Leucine",
            "UCU" or "UCC" or "UCA" or "UCG" => "Serine",
            "UAU" or "UAC" => "Tyrosine",
            "UGU" or "UGC" => "Cysteine",
            "UGG" => "Tryptophan",
            "UAA" or "UAG" or "UGA" => "STOP",
            _ => throw new Exception("Unknown codon")
        };
}