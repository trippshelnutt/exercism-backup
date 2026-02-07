using System;
using System.Text;

public static class Identifier
{
    public static string Clean(string identifier)
    {
        var builder = new StringBuilder();
        var upperCaseNext = false;

        foreach (var c in identifier)
        {
            builder.Append(c switch
            {
                _ when (c >= 'α' && c <= 'ω') => string.Empty,
                _ when upperCaseNext => char.ToUpperInvariant(c),
                _ when char.IsWhiteSpace(c) => '_',
                _ when char.IsControl(c) => "CTRL",
                _ when char.IsLetter(c) => c,
                _ => string.Empty
            });
        
            upperCaseNext = (c == '-');
        }

        return builder.ToString();
    }
}
