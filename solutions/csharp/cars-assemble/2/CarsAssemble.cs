using System;

static class AssemblyLine
{
    private const int NumberOfCarsPerHour = 221;

    public static double SuccessRate(int speed)
        => speed switch
        {
            0 => 0,
            < 5 => 1.0,
            < 9 => 0.9,
            9 => 0.8,
            10 => 0.77,
            _ => throw new Exception("Speed out of range")
        };

    public static double ProductionRatePerHour(int speed)
        => speed * SuccessRate(speed) * NumberOfCarsPerHour;

    public static int WorkingItemsPerMinute(int speed)
        => (int)(ProductionRatePerHour(speed) / 60);
}
