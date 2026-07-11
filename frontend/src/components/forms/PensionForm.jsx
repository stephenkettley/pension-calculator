import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";

import Button from "../common/Button";
import Card from "../common/Card";
import Input from "../common/Input";

import { pensionSchema } from "../../schemas/pensionSchema";
import { calculatePension } from "../../services/pensionService";

function PensionForm({ onCalculate }) {
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
      onCalculate(data, result);  
    } catch (error) {
      console.error(error);
    }
  };

  return (
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
  );
}

export default PensionForm;