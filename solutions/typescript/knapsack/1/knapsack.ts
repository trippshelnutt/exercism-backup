type Item = {
  weight: number
  value: number
}

export function maximumValue({
  maximumWeight,
  items,
}: {
  maximumWeight: number
  items: Item[]
}): number {
  // Create a 2D DP table: dp[i][w] = max value using first i items with weight limit w
  const dp: number[][] = Array(items.length + 1)
    .fill(null)
    .map(() => Array(maximumWeight + 1).fill(0))

  // Fill the DP table
  for (let i = 1; i <= items.length; i++) {
    const { weight, value } = items[i - 1]
    for (let w = 0; w <= maximumWeight; w++) {
      // Option 1: don't take the current item
      dp[i][w] = dp[i - 1][w]

      // Option 2: take the current item (if it fits)
      if (weight <= w) {
        dp[i][w] = Math.max(dp[i][w], dp[i - 1][w - weight] + value)
      }
    }
  }

  return dp[items.length][maximumWeight]
}
