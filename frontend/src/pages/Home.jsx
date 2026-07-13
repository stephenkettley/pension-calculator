import { useState } from "react";

import PensionForm from "../components/forms/PensionForm";
import PensionResults from "../components/results/PensionResults";

function Home() {
  const [inputs, setInputs] = useState(null); // these are tracked in high level page because they feed to form and results
  const [calculation, setCalculation] = useState(null); // this controls view of form or results

  const handleCalculation = (formData, result) => {
    setInputs(formData);
    setCalculation(result);
  };

  const handleReset = () => {
    setCalculation(null);
  };

  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-200 via-white to-sky-900">
      <div
        className={`mx-auto flex min-h-screen items-center px-6 py-16 ${
          calculation ? "max-w-7xl" : "max-w-3xl"
        }`}
      >
        <div className="w-full">
          <h1 className="mb-1 text-center text-8xl tracking-tight font-delight">
            <span className="font-bold text-sky-900">Pension</span>
            <span className="font-normal text-black">Pearl</span>
          </h1>

          <h1 className="mb-8 text-center text-3xl tracking-tight font-delight font-normal">
            Helping you plan your financial freedom.
          </h1>

          {!calculation && (
            <p className="mt-10 mb-10 text-center text-md leading-relaxed text-slate-600">
              Enter your retirement details to see how your pension could grow
              over time, including your projected retirement balance, total
              contributions, and investment growth.
            </p>
          )}

          {/* conditional home page rendering */}
          {!calculation ? (
            <PensionForm
              onCalculate={handleCalculation}
              defaultValues={inputs}
            />
          ) : (
            <PensionResults
              data={calculation}
              inputs={inputs}
              onReset={handleReset}
            />
          )}
        </div>
      </div>
    </main>
  );
}

export default Home;