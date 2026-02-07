using System;

static class AssemblyLine
{
    private const int NumberOfCarsPerHour = 221;

    public static double SuccessRate(int speed)
        => speed switch
        {
            var s when s == 0 => 0,
            var s when s < 5 => 1.0,
            var s when s < 9 => 0.9,
            var s when s == 9 => 0.8,
            _ => 0.77
        };

    public static double ProductionRatePerHour(int speed)
        => speed * SuccessRate(speed) * NumberOfCarsPerHour;

    public static int WorkingItemsPerMinute(int speed)
        => (int)(ProductionRatePerHour(speed) / 60);
}
