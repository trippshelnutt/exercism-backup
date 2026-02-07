using System;
using System.Text.RegularExpressions;

static class LogLine
{
    private const string Pattern = "\\[(.+)\\]:(.+)";

    public static string Message(string logLine)
        => Regex.Match(logLine, Pattern).Groups[2].Captures[0].Value.Trim();

    public static string LogLevel(string logLine)
        => Regex.Match(logLine, Pattern).Groups[1].Captures[0].Value.ToLower();

    public static string Reformat(string logLine)
        => $"{Message(logLine)} ({LogLevel(logLine)})";
}
