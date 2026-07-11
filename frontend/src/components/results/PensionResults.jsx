import { formatCurrency } from "../../utils/formatters";
import Card from "../common/Card";

function PensionResults({ data }) {
  if (!data) {
    return null;
  }

  return (
    <Card>
      <h2 className="text-2xl font-semibold mb-6">
        Your Pension Projection
      </h2>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div className="border rounded-lg p-4 flex flex-col items-center">
          <p className="text-sm text-gray-500 mb-1 text-center">
            Projected Retirement Balance
          </p>
          <p className="text-3xl font-bold text-center">
            {formatCurrency(data.projected_balance)}
          </p>
        </div>

        <div className="border rounded-lg p-4 flex flex-col items-center">
          <p className="text-sm text-gray-500 mb-1 text-center">
            Total Contributions
          </p>
          <p className="text-xl font-semibold text-center">
            {formatCurrency(data.total_contributions)}
          </p>
        </div>

        <div className="border rounded-lg p-4 flex flex-col items-center">
          <p className="text-sm text-gray-500 mb-1 text-center">
            Investment Growth
          </p>
          <p className="text-xl font-semibold text-center">
            {formatCurrency(data.total_growth)}
          </p>
        </div>

        <div className="border rounded-lg p-4 flex flex-col items-center">
          <p className="text-sm text-gray-500 mb-1 text-center">
            Years Until Retirement
          </p>
          <p className="text-xl font-semibold text-center">
            {data.years_to_retirement} years
          </p>
        </div>
      </div>
    </Card>
  );
}

export default PensionResults;