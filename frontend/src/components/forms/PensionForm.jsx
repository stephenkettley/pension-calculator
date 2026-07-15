import { zodResolver } from "@hookform/resolvers/zod";
import { useState } from "react";
import { useForm } from "react-hook-form";

import Button from "../common/Button";
import Card from "../common/Card";
import Input from "../common/Input";

import { pensionSchema } from "../../schemas/pensionSchema";
import { calculatePension } from "../../services/pensionService";

function PensionForm({ onCalculate, defaultValues }) {
  const [useTargetAmount, setUseTargetAmount] = useState(
    defaultValues?.useTargetAmount ?? false
  );

  const formDefaults = defaultValues
    ? {
        currentAge: String(defaultValues.currentAge),
        retirementAge: String(defaultValues.retirementAge),
        currentBalance: String(defaultValues.currentBalance),
        pensionValue: String(
          defaultValues.pensionValue ?? ""
        ),
        annualGrowthRate: String(defaultValues.annualGrowthRate),
      }
    : undefined;

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(pensionSchema),
    defaultValues: formDefaults,
  });

  const onSubmit = async (data) => {
    try {
      const result = await calculatePension(
        data,
        useTargetAmount
      );
      console.log(result);
      onCalculate(
        {
          ...data,
          useTargetAmount,
        },
        result
      );
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


        <div className="flex items-center gap-2">
          <input
            id="useTargetAmount"
            type="checkbox"
            checked={useTargetAmount}
            onChange={(e) =>
              setUseTargetAmount(e.target.checked)
            }
            className="h-4 w-4 rounded border-slate-300 text-sky-900 focus:ring-sky-900"
          />

          <label
            htmlFor="useTargetAmount"
            className="text-sm text-slate-700"
          >
            I would rather provide a specific end goal for my pension.
          </label>
        </div>

        <Input
          label={
            useTargetAmount
              ? "Target Retirement Amount"
              : "Annual Contribution"
          }
          name="pensionValue"
          type="number"
          error={
            errors.pensionValue && {
              ...errors.pensionValue,
              message: errors.pensionValue.message.replace(
                "Pension value",
                useTargetAmount
                  ? "Target retirement amount"
                  : "Annual contribution"
              ),
            }
          }
          {...register("pensionValue")}
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
          Calculate My Pension Projections
        </Button>
      </form>
    </Card>
  );
}

export default PensionForm;