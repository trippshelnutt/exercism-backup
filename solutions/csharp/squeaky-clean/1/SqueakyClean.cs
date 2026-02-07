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
            if (upperCaseNext)
            {
                builder.Append(c.ToString().ToUpper());
                upperCaseNext = false;
            }
            else if (c == ' ')
            {
                builder.Append("_");
            }
            else if (char.IsControl(c))
            {
                builder.Append("CTRL");
            }
            else if (c == '-')
            {
                upperCaseNext = true;
            }
            else if (c < 'α' || c > 'ω')
            {
                builder.Append(c);
            }
        }

        return builder.ToString();
    }
}
