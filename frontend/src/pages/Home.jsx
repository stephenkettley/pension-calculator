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
    <main className="min-h-screen bg-gradient-to-b from-slate-200 via-white to-sky-900">
  
      <div
        className={`mx-auto flex min-h-screen items-center px-6 py-16 ${
          calculation ? "max-w-7xl" : "max-w-3xl"
        }`}
      >
  
        <div className="w-full">
  
        <h1 className="mb-3 text-center text-8xl tracking-tight font-delight">
          <span className="font-bold text-sky-900">Pension</span>
          <span className="font-normal text-black">Pearl</span>
        </h1>

        <h1 className="mb-8 mt-2 text-center font-bold text-2xl">Discover the power of long-term wealth</h1>
  
          {!calculation && (
            <p className="mt-10 mb-10 text-center text-md leading-relaxed text-slate-600">
              Provide your retirement information to receive a detailed forecast of your pension growth, investment performance, and projected retirement fund value.
            </p>
          )}
     
          
  
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