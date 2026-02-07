using System;

public class Player
{
    private const int MinDieRoll = 1;
    private const int MaxDieRoll = 18;
    private const double MaxSpellStrength = 100.0;

    private Random random = new Random();

    public int RollDie()
        => random.Next(MinDieRoll, MaxDieRoll + 1);

    public double GenerateSpellStrength()
        => random.NextDouble() * MaxSpellStrength;
}
