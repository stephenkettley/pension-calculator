// this will pull in from Vercel for production
const API_BASE_URL = import.meta.env.VITE_API_URL;

export async function calculatePension(
  data,
  useTargetAmount = false
) {
  const endpoint = useTargetAmount
    ? "/pension/calculate_contribution"
    : "/pension/calculate_pension";

  const body = useTargetAmount
    ? {
        current_age: data.currentAge,
        retirement_age: data.retirementAge,
        current_balance: data.currentBalance,
        target_amount: data.pensionValue,
        annual_growth_rate: data.annualGrowthRate,
        contribution_frequency: "annual",
      }
    : {
        current_age: data.currentAge,
        retirement_age: data.retirementAge,
        current_balance: data.currentBalance,
        contribution_amount: data.pensionValue,
        annual_growth_rate: data.annualGrowthRate,
        contribution_frequency: "annual",
      };

  const response = await fetch(
    `${API_BASE_URL}${endpoint}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
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