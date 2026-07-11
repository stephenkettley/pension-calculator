import PensionForm from "../components/forms/PensionForm";

function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-100 via-white to-sky-100">
      <div className="mx-auto flex min-h-screen max-w-3xl items-center px-6 py-16">
        <div className="w-full">
          <h1 className="mb-3 text-center text-5xl font-bold tracking-tight text-slate-900">
            Pension Calculator
          </h1>

          <p className="mb-10 text-center text-lg leading-relaxed text-slate-600">
            Estimate how your retirement savings could grow over time based on
            your current balance, annual contributions, and expected investment
            returns.
          </p>

          <PensionForm />
        </div>
      </div>
    </main>
  );
}

export default Home;