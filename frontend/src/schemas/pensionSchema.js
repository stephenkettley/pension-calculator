import { z } from "zod";

const numberField = (name) =>
  z
    .string()
    .trim()
    .min(1, `${name} is required.`)
    .transform((value) => Number(value))
    .pipe(
      z.number().finite(`${name} is required.`)
    );

export const pensionSchema = z
  .object({
    currentAge: numberField("Current age")
      .pipe(
        z
          .number()
          .int("Current age must be a whole number.")
          .min(
            18,
            "You must be at least 18 years old."
          )
      ),

    retirementAge: numberField("Retirement age")
      .pipe(
        z
          .number()
          .int("Retirement age must be a whole number.")
          .min(
            18,
            "Retirement age must be at least 18."
          )
      ),

    currentBalance: numberField("Current balance")
      .pipe(
        z
          .number()
          .int("Current balance must be a whole number.")
          .min(
            0,
            "Current balance cannot be negative."
          )
      ),

    contributionAmount: numberField("Annual contribution")
      .pipe(
        z
          .number()
          .int("Annual contribution must be a whole number.")
          .min(
            0,
            "Annual contribution cannot be negative."
          )
      ),

    annualGrowthRate: numberField("Annual growth rate")
      .pipe(
        z
          .number()
          .gt(
            0,
            "Annual growth rate must be greater than zero."
          )
          .max(
            100,
            "Annual growth rate must be less than or equal to 100."
          )
      ),
  })
  .refine(
    (data) => data.retirementAge > data.currentAge,
    {
      path: ["retirementAge"],
      message:
        "Retirement age must be greater than your current age.",
    }
  );