import { useState } from "react";

import Button from "../common/Button";
import Card from "../common/Card";
import Input from "../common/Input";

function PensionForm() {
  const [formData, setFormData] = useState({
    currentAge: "",
    retirementAge: "",
    currentBalance: "",
    contributionAmount: "",
    annualGrowthRate: "",
  });

  function handleChange(event) {
    const { name, value } = event.target;

    setFormData((previousData) => ({
      ...previousData,
      [name]: value,
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();

    console.log(formData);
  }

  return (
    <Card>
      <form
        onSubmit={handleSubmit}
        className="space-y-6"
      >
        <Input
          label="Current Age"
          name="currentAge"
          type="number"
          min={18}
          max={100}
          value={formData.currentAge}
          onChange={handleChange}
          required
        />

        <Input
          label="Retirement Age"
          name="retirementAge"
          type="number"
          min={18}
          max={100}
          value={formData.retirementAge}
          onChange={handleChange}
          required
        />

        <Input
          label="Current Balance"
          name="currentBalance"
          type="number"
          min={0}
          step="0.01"
          value={formData.currentBalance}
          onChange={handleChange}
          required
        />

        <Input
          label="Annual Contributions"
          name="contributionAmount"
          type="number"
          min={0}
          step="0.01"
          value={formData.contributionAmount}
          onChange={handleChange}
          required
        />

        <Input
          label="Annual Growth Rate (%)"
          name="annualGrowthRate"
          type="number"
          min={0}
          max={100}
          step="0.1"
          value={formData.annualGrowthRate}
          onChange={handleChange}
          required
        />

        <Button type="submit">
          Calculate My Pension
        </Button>
      </form>
    </Card>
  );
}

export default PensionForm;