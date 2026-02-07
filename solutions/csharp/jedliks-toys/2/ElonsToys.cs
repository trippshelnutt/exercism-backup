using System;

class RemoteControlCar
{
    private const int StartingDistanceInMeters = 0;
    private const int StartingBatteryChargePercent = 100;
    private const int DistanceInMetersPerDrive = 20;
    private const int BatteryChargePercentPerDrive = 1;
    private const int MinimumBatteryChargePercent = 0;

    private int DistanceDrivenInMeters = StartingDistanceInMeters;
    private int BatteryChargePercent = StartingBatteryChargePercent;

    public static RemoteControlCar Buy() => new();

    public string DistanceDisplay()
        => $"Driven {DistanceDrivenInMeters} meters";

    public string BatteryDisplay()
        => BatteryChargePercent > MinimumBatteryChargePercent
            ? $"Battery at {BatteryChargePercent}%"
            : "Battery empty";

    public void Drive()
    {
        if (BatteryChargePercent > MinimumBatteryChargePercent)
        {
            DistanceDrivenInMeters += DistanceInMetersPerDrive; 
            BatteryChargePercent -= BatteryChargePercentPerDrive;
        }
    }
}
