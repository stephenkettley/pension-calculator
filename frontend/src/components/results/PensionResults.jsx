import { formatCurrency } from "../../utils/formatters";

import PensionGrowthChart from "../charts/PensionGrowthChart";
import Button from "../common/Button";
import Card from "../common/Card";

function PensionResults({ data, inputs, onReset }) {
  if (!data) {
    return null;
  }

  // very basic percentage calculations
  const contributionPercentage = Math.round(
    (data.total_contributions / data.projected_balance) * 100
  );

  const growthPercentage = 100 - contributionPercentage;

  return (
    <Card>
      <h2 className="mb-3 text-2xl font-semibold">
        Your Pension Projection
      </h2>

      <p className="mb-8 text-sm">
        Your estimated pension projections, calculated using your custom inputs,
        are shown below.
      </p>

      <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
        {/* Inputs */}
        <div className="rounded-lg border p-5">
          <h3 className="mb-4 text-lg font-semibold">
            Your Specified Inputs
          </h3>

          <div className="space-y-4 text-sm">
            <div>
              <p className="text-gray-500">Current Age</p>
              <p className="font-semibold">{inputs.currentAge} years</p>
            </div>

            <div>
              <p className="text-gray-500">Retirement Age</p>
              <p className="font-semibold">{inputs.retirementAge} years</p>
            </div>

            <div>
              <p className="text-gray-500">Current Balance</p>
              <p className="font-semibold">
                {formatCurrency(inputs.currentBalance)}
              </p>
            </div>

            <div>
              <p className="text-gray-500">Annual Contribution</p>
              <p className="font-semibold">
                {formatCurrency(inputs.contributionAmount)}
              </p>
            </div>

            <div>
              <p className="text-gray-500">Annual Growth Rate</p>
              <p className="font-semibold">
                {inputs.annualGrowthRate}%
              </p>
            </div>
          </div>

          <Button
            onClick={onReset}
          >
            Adjust Inputs
          </Button>
        </div>

        {/* Results */}
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:col-span-2">
          <div className="flex min-h-32 flex-col items-center justify-center rounded-xl border p-6 text-center">
            <p className="mb-3 text-base font-medium text-gray-500">
              Projected Retirement Balance
            </p>

            <p className="text-3xl font-bold text-green-500">
              {formatCurrency(data.projected_balance)}
            </p>
          </div>

          <div className="flex min-h-32 flex-col items-center justify-center rounded-xl border p-6 text-center">
            <p className="mb-3 text-base font-medium text-gray-500">
              Years Until Retirement
            </p>

            <p className="text-3xl font-semibold">
              {data.years_to_retirement} years
            </p>
          </div>

          <div className="flex min-h-32 flex-col items-center justify-center rounded-xl border p-6 text-center">
            <p className="mb-3 text-base font-medium text-gray-500">
              Total Contributions
            </p>

            <p className="text-3xl font-semibold">
              {formatCurrency(data.total_contributions)}
            </p>

            <p className="mt-2 text-sm italic text-gray-500">
              {contributionPercentage}% of your total balance
            </p>
          </div>

          <div className="flex min-h-32 flex-col items-center justify-center rounded-xl border p-6 text-center">
            <p className="mb-3 text-base font-medium text-gray-500">
              Total Investment Growth
            </p>

            <p className="text-3xl font-semibold">
              {formatCurrency(data.total_growth)}
            </p>

            <p className="mt-2 text-sm italic text-gray-500">
              {growthPercentage}% of your total balance
            </p>
          </div>
        </div>
      </div>

      {/* Graph */}
      <div className="mt-10 rounded-xl border p-6">
        <h3 className="mb-6 text-xl font-semibold">
          Projected Contributions and Investment Growth by Age
        </h3>

        <PensionGrowthChart projection={data.projection} />
      </div>
    </Card>
  );
}

export default PensionResults;