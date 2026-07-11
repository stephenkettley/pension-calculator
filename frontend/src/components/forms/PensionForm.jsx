import { zodResolver } from "@hookform/resolvers/zod";
import { useState } from "react";
import { useForm } from "react-hook-form";

import Button from "../common/Button";
import Card from "../common/Card";
import Input from "../common/Input";
import PensionResults from "../results/PensionResults";

import { pensionSchema } from "../../schemas/pensionSchema";
import { calculatePension } from "../../services/pensionService";

function PensionForm() {
  const [calculation, setCalculation] = useState(null);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(pensionSchema),
  });

  const onSubmit = async (data) => {
    try {
      const result = await calculatePension(data);

      setCalculation(result);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      {!calculation ? (
        <Card>
          <form
            noValidate
            onSubmit={handleSubmit(onSubmit)}
            className="space-y-6"
          >
            <Input
              label="Current Age"
              name="currentAge"
              type="number"
              error={errors.currentAge}
              {...register("currentAge")}
            />
  
            <Input
              label="Retirement Age"
              name="retirementAge"
              type="number"
              error={errors.retirementAge}
              {...register("retirementAge")}
            />
  
            <Input
              label="Current Balance"
              name="currentBalance"
              type="number"
              error={errors.currentBalance}
              {...register("currentBalance")}
            />
  
            <Input
              label="Annual Contribution"
              name="contributionAmount"
              type="number"
              error={errors.contributionAmount}
              {...register("contributionAmount")}
            />
  
            <Input
              label="Annual Growth Rate (%)"
              name="annualGrowthRate"
              type="number"
              step="0.1"
              error={errors.annualGrowthRate}
              {...register("annualGrowthRate")}
            />
  
            <Button type="submit">
              Calculate My Pension
            </Button>
          </form>
        </Card>
      ) : (
        <PensionResults data={calculation} />
      )}
    </>
  );
}

export default PensionForm;