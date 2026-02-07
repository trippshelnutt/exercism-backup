class Lasagna
{
    private const int CookTimeInMinutes = 40;
    private const int PrepTimePerLayerInMinutes = 2;

    public int ExpectedMinutesInOven() => CookTimeInMinutes;

    public int RemainingMinutesInOven(int actualMinutesInOven) => ExpectedMinutesInOven() - actualMinutesInOven;

    public int PreparationTimeInMinutes(int layers) => layers * PrepTimePerLayerInMinutes;

    public int ElapsedTimeInMinutes(int layers, int actualMinutesInOven) => PreparationTimeInMinutes(layers) + actualMinutesInOven;
}
