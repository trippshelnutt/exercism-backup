using System;

static class LogLine
{
    private const int LogLevelIndex = 0;
    private const int MessageIndex = 1;

    public static string Message(string logLine)
    {
        var logParts = GetLogParts(logLine);
        var message = logParts[MessageIndex].Trim();
        return message;
    }

    public static string LogLevel(string logLine)
    {
        var logParts = GetLogParts(logLine);
        var logLevel = logParts[LogLevelIndex].Replace("[", "").Replace("]","").ToLower();
        return logLevel;
    }

    public static string Reformat(string logLine)
        => $"{Message(logLine)} ({LogLevel(logLine)})";

    private static string[] GetLogParts(string logLine)
        => logLine.Split(':');
}
