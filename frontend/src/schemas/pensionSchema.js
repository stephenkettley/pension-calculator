import { z } from "zod";

export const pensionSchema = z
  .object({
    currentAge: z
      .number({
        required_error: "Current age is required.",
        invalid_type_error: "Current age is required.",
      })
      .min(18, "You must be at least 18 years old."),

    retirementAge: z
      .number({
        required_error: "Retirement age is required.",
        invalid_type_error: "Retirement age is required.",
      })
      .min(18, "Retirement age must be at least 18."),

    currentBalance: z
      .number({
        required_error: "Current balance is required.",
        invalid_type_error: "Current balance is required.",
      })
      .min(0, "Current balance cannot be negative."),

    contributionAmount: z
      .number({
        required_error: "Annual contribution is required.",
        invalid_type_error: "Annual contribution is required.",
      })
      .min(0, "Annual contribution cannot be negative."),

    annualGrowthRate: z
      .number({
        required_error: "Annual growth rate is required.",
        invalid_type_error: "Annual growth rate is required.",
      })
      .gt(0, "Annual growth rate must be greater than zero."),
  })
  .refine(
    (data) => data.retirementAge > data.currentAge,
    {
      path: ["retirementAge"],
      message: "Retirement age must be greater than your current age.",
    }
  );