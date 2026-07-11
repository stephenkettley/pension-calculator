import { formatCurrency } from "../../utils/formatters";

import PensionGrowthChart from "../charts/PensionGrowthChart";
import Card from "../common/Card";


function PensionResults({ data, inputs, onReset }) {

  if (!data) {
    return null;
  }


  return (

    <Card>

      <h2 className="text-2xl font-semibold mb-6">
        Your Pension Projection
      </h2>



      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">


        {/* Assumptions */}

        <div className="rounded-lg border p-5">

          <h3 className="text-lg font-semibold mb-4">
            Your Custom Inputs
          </h3>


          <div className="space-y-4 text-sm">


            <div>
              <p className="text-gray-500">
                Current Age
              </p>

              <p className="font-semibold">
                {inputs.currentAge} years
              </p>
            </div>



            <div>
              <p className="text-gray-500">
                Retirement Age
              </p>

              <p className="font-semibold">
                {inputs.retirementAge} years
              </p>
            </div>



            <div>
              <p className="text-gray-500">
                Current Balance
              </p>

              <p className="font-semibold">
                {formatCurrency(inputs.currentBalance)}
              </p>
            </div>



            <div>
              <p className="text-gray-500">
                Annual Contribution
              </p>

              <p className="font-semibold">
                {formatCurrency(inputs.contributionAmount)}
              </p>
            </div>



            <div>
              <p className="text-gray-500">
                Annual Growth Rate
              </p>

              <p className="font-semibold">
                {inputs.annualGrowthRate}%
              </p>
            </div>


          </div>

        </div>





        {/* Results */}

        <div className="lg:col-span-2 grid grid-cols-1 sm:grid-cols-2 gap-6">


          <div className="border rounded-xl p-6 flex flex-col items-center justify-center text-center min-h-32">

            <p className="text-sm text-gray-500 mb-3">
              Projected Retirement Balance
            </p>

            <p className="text-2xl text-green-500 font-bold">
              {formatCurrency(data.projected_balance)}
            </p>

          </div>




          <div className="border rounded-xl p-6 flex flex-col items-center justify-center text-center min-h-32">

            <p className="text-sm text-gray-500 mb-3">
              Total Contributions
            </p>

            <p className="text-2xl font-semibold">
              {formatCurrency(data.total_contributions)}
            </p>

          </div>





          <div className="border rounded-xl p-6 flex flex-col items-center justify-center text-center min-h-32">

            <p className="text-sm text-gray-500 mb-3">
              Investment Growth
            </p>

            <p className="text-2xl font-semibold">
              {formatCurrency(data.total_growth)}
            </p>

          </div>





          <div className="border rounded-xl p-6 flex flex-col items-center justify-center text-center min-h-32">

            <p className="text-sm text-gray-500 mb-3">
              Years Until Retirement
            </p>

            <p className="text-2xl font-semibold">
              {data.years_to_retirement} years
            </p>

          </div>


        </div>


      </div>





      {/* Graph */}

      <div className="mt-10 border rounded-xl p-6">


        <h3 className="text-xl font-semibold mb-6">
          Growth Projection
        </h3>



        <PensionGrowthChart
          projection={data.projection}
        />


      </div>





      {/* Reset Button */}

      <div className="mt-8">

        <button
          onClick={onReset}
          className="
            w-full
            rounded-lg
            border
            px-6
            py-3
            font-semibold
            transition
            hover:bg-slate-100
          "
        >
          Calculate Again
        </button>

      </div>


    </Card>

  );

}


export default PensionResults;