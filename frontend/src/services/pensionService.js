// this will pull in from Vercel for production
const API_BASE_URL = import.meta.env.VITE_API_URL; 

export async function calculatePension(data) {
  const response = await fetch(
    `${API_BASE_URL}/pension/calculate_pension`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        current_age: data.currentAge,
        retirement_age: data.retirementAge,
        current_balance: data.currentBalance,
        contribution_amount: data.contributionAmount,
        contribution_frequency: "annual",
        annual_growth_rate: data.annualGrowthRate,
      }),
    }
  );

  if (!response.ok) {
    const errorData = await response.json();

    throw new Error(
      errorData.message ||
      "Failed to calculate pension."
    );
  }

  return await response.json();
}