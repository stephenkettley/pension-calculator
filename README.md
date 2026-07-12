<img width="1500" height="600" alt="pension-pearl-logo" src="https://github.com/user-attachments/assets/bd8474b3-71c5-4930-9bde-ca2da1619ea9" />

# PensionPearl
<br><br>

## Project Overview
PensionPearl is a simple, yet extremely useful full-stack retirement planning application designed to help users estimate how their pension savings could grow over time based on their current balance, planned contributions, expected investment returns, and retirement timeline.  The application provides an intuitive way to explore future retirement outcomes through interactive visualisations and clear financial summaries, while also presenting an inflation-adjusted estimate of future purchasing power. It is intended as an educational planning tool that helps users understand the long-term impact of saving and investing, rather than providing personalised financial advice or replacing professional financial planning. The primary goal of the project was to demonstrate clean full-stack software engineering principles, thoughtful user experience design, robust validation, automated testing, and a production-ready deployment pipeline.
<br><br>

## Links To View Project
Working application: https://pension-calculator-pearl.vercel.app/ <br>
Backend API Documentation: https://pension-calculator-api-b1de48aa93f1.herokuapp.com/docs
<br><br>

## Features
- Retirement projection calculator
- Inflation-adjusted purchasing power
- Annual contribution tracking
- Interactive growth chart
- Client & server validation
- Fully deployed frontend and backend
- Automated CI/CD
- Unit and API testing
- Logging
- Exception handling
<br><br>

## Engineering Decisions
Although this project is intentionally small in scope, it was designed using many of the same engineering principles I would apply when building a larger production system.

- Separated business logic from API routes to improve maintainability, readability, and testability.
- Kept the frontend stateless by performing all financial calculations on the backend, ensuring a single source of truth for business logic.
- Implemented strong typing throughout both the frontend and backend to improve reliability and reduce runtime errors.
- Applied validation at multiple layers, including both client-side and server-side validation, to ensure data integrity.
- Automated testing and deployment to ensure changes are validated before being released.
- Deployed the frontend and backend independently to better reflect a modern production architecture.
- Structured the project into clear layers with a separation between presentation, API, business logic, and configuration.
- Prioritised readable, maintainable code over overly clever implementations, making the project easier to extend and test.
- Designed the application so that business logic remains reusable and independent of the API layer, allowing it to be consumed by other interfaces in the future if required.
<br><br>

## Assumptions
To keep the scope focused and the calculator simple to use, the following assumptions were made:

- Users are **18 years or older**.
- Retirement age must be **greater than the current age**.
- Contributions remain **constant** throughout the investment period.
- The annual investment growth rate remains **constant** over the investment period.
- Investment growth is **compounded monthly** using an effective monthly growth rate.
- Inflation is assumed to average **5% per year** when estimating the purchasing power of the projected retirement balance.
- Contributions are assumed to be made at the **end of each month**.
- Taxes, investment fees, employer contributions, salary increases, and legislative changes are **not included**.
- The calculator is intended as an **educational retirement planning tool** to help users understand long-term investment growth rather than provide personalised financial advice.
<br><br>

## Time Spent
Approximately **6–8 hours**.

- **3–4 hours** were spent developing the core full-stack pension calculator, including the required functionality, API, frontend, validation, and retirement calculations.
- **2–4 additional hours** were invested in taking the project beyond the minimum requirements to better demonstrate my engineering approach. This included:
  - Project setup and environment configuration.
  - Debugging and deployment issues encountered during development.
  - Setting up automated CI/CD and cloud deployments.
  - Expanding automated testing.
  - Refining the UI/UX and overall user experience.
  - Writing comprehensive documentation, including a detailed README and local setup instructions.
  - Using AI as a review and productivity tool to challenge implementation decisions, identify potential improvements, and help polish the project to a production-ready standard.

The core project requirements were completed within the expected timeframe. The additional time was intentionally invested to produce a more complete, maintainable, and professional project that better reflects how I approach software engineering beyond simply delivering the minimum functionality.
<br><br>

## Tools & Technologies
- **React:** A component-based frontend library that makes it easy to build responsive, reusable, and maintainable user interfaces.
- **FastAPI:** A modern Python web framework offering excellent performance, strong type safety, and automatic API documentation.
- **Pydantic:** Provides robust data validation and parsing with minimal boilerplate while enforcing type safety.
- **Chart.js:** Enables clear, interactive visualisations of retirement projections and investment growth over time.
- **React Hook Form:** Efficiently manages form state with minimal re-renders and built-in validation support.
- **Zod:** Provides declarative, type-safe client-side validation that integrates seamlessly with React Hook Form.
- **Pytest:** A lightweight and expressive testing framework used to validate business logic and API behaviour.
- **GitHub Actions:** Automates testing and deployment to ensure every change is validated before release.
- **Heroku:** A simple cloud platform for deploying and hosting the FastAPI backend with minimal configuration.
- **Vercel:** Optimised for deploying React applications with automatic builds and seamless GitHub integration.
<br><br>

## Architecture Overview

The application follows a simple client-server architecture.

The React frontend is responsible for collecting user input, performing client-side validation and displaying the calculated results. Requests are sent to the FastAPI backend, where Pydantic validates incoming data before the calculation service performs all business logic.

The backend returns structured JSON responses which are rendered into summary cards and interactive charts on the frontend.

The project uses GitHub Actions to automate testing and deployment, with the backend hosted on **Heroku** and the frontend hosted on **Vercel**.
<br><br>

## How AI Was Used
AI was used throughout the project as a productivity, learning, and review tool rather than as a replacement for software engineering knowledge or decision-making. My approach was to first understand the project requirements, design the solution myself, and then use AI to challenge my thinking, accelerate implementation, and improve the overall quality of the project.

I believe one of AI's greatest strengths is its ability to **refine engineering work rather than replace engineering thinking**. It can help uncover edge cases, identify potential improvements, suggest alternative implementations, and increase the overall robustness of a solution. Used responsibly, AI acts as another experienced engineer reviewing your work, helping to produce cleaner, more reliable software while still requiring the developer to understand, evaluate, and ultimately own every implementation decision.

AI was used to:

- **Challenge design decisions:** After planning the project architecture and identifying the core functionality, I used AI to question my design choices and suggest alternative approaches. I intentionally rejected ideas that expanded the project beyond the intended scope while adopting simple improvements that added value.
- **Accelerate front-end development:** Used AI to assist with component styling, layout refinement, and general UI improvements, allowing more time to focus on application architecture and business logic.
- **Generate and expand test cases:** Used AI to suggest additional backend test scenarios and edge cases that I may not have initially considered, improving overall test coverage.
- **Assist with writing tests:** Used AI to help implement repetitive test cases more quickly while ensuring I understood and reviewed every generated test before including it in the project.
- **Review application code:** Used AI to identify potential edge cases, improve readability, simplify implementations where appropriate, and suggest more maintainable solutions.
- **Improve exception handling:** Used AI to refactor the initial exception handling into a more robust global exception handling approach using FastAPI best practices.
- **Refine deployment and infrastructure:** Used AI to assist with debugging deployment issues, refining GitHub Actions workflows, improving deployment configuration, and ensuring the frontend and backend deployment pipelines were reliable.
- **Improve project configuration:** Used AI to review configuration files and suggest cleaner, more maintainable project setup where appropriate.
- **Polish documentation:** Used AI as an editing and review tool to improve the clarity and completeness of the project documentation.

The area where AI contributed the least was the **backend implementation and business logic**. Backend engineering is one of my strongest technical areas, so I intentionally designed and implemented the API, validation, calculations, architecture, and overall backend structure myself. AI was primarily used as a reviewer to challenge implementation decisions and identify possible improvements rather than to generate the core backend solution.

Throughout the project, every AI-generated suggestion was reviewed, understood, and, where appropriate, modified before being incorporated. AI was treated as an engineering assistant that accelerated development and strengthened the overall quality of the project, while all architectural decisions, implementation choices, and final code ownership remained my responsibility.
<br><br>


