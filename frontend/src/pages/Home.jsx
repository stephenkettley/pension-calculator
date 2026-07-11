import { useState } from "react";

import PensionForm from "../components/forms/PensionForm";
import PensionResults from "../components/results/PensionResults";


function Home() {

  const [inputs, setInputs] = useState(null);
  const [calculation, setCalculation] = useState(null);


  const handleCalculation = (formData, result) => {
    setInputs(formData);
    setCalculation(result);
  };


  const handleReset = () => {
    setInputs(null);
    setCalculation(null);
  };


  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-100 via-white to-sky-100">
  
      <div
        className={`mx-auto flex min-h-screen items-center px-6 py-16 ${
          calculation ? "max-w-7xl" : "max-w-3xl"
        }`}
      >
  
        <div className="w-full">
  
          <h1 className="mb-3 text-center text-5xl font-bold tracking-tight text-slate-900">
            Pension Calculator
          </h1>
  
          <p className="mb-10 text-center text-lg leading-relaxed text-slate-600">
            Estimate how your retirement savings could grow over time based on
            your current balance, annual contributions, and expected investment
            returns.
          </p>
  
          {!calculation ? (
            <PensionForm
              onCalculate={handleCalculation}
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