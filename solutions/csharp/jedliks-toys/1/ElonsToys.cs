using System;

class RemoteControlCar
{
    private int DistanceDrivenInMeters = 0;
    private int BatteryChargePercent = 100;

    public static RemoteControlCar Buy()
        => new RemoteControlCar();

    public string DistanceDisplay()
        => $"Driven {DistanceDrivenInMeters} meters";

    public string BatteryDisplay()
        => BatteryChargePercent > 0
            ? $"Battery at {BatteryChargePercent}%"
            : "Battery empty";

    public void Drive()
    {
        if (BatteryChargePercent > 0)
        {
            DistanceDrivenInMeters += 20;
            BatteryChargePercent -= 1;
        }
    }
}
