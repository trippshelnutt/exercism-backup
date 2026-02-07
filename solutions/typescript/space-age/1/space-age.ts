type EarthYearMapType = {
  [id: string]: number;
}

const earthYearMap: EarthYearMapType = {
  'mercury': 0.2408467,
  'venus': 0.61519726,
  'earth': 1,
  'mars': 1.8808158,
  'jupiter': 11.862615,
  'saturn': 29.447498,
  'uranus': 84.016846,
  'neptune': 164.79132,
};

const secondsInAYear: number = 365.25 * 24 * 60 * 60;

export function age(planet: string, seconds: number): number {
  const years = seconds / secondsInAYear;
  return +(years / earthYearMap[planet]).toFixed(2);
}
