<img width="1500" height="600" alt="pp-logo" src="https://github.com/user-attachments/assets/0fe4ab47-c7a6-4599-bdab-6d7fb37c5fcf" />

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
<<<<<<< HEAD
Approximately **6–8 hours**.
=======
Approximately **6 hours**.
>>>>>>> origin/main

- **3–4 hours** were spent developing the core full-stack pension calculator, including the required functionality, API, frontend, validation, and retirement calculations.
- **2–4 additional hours** were invested in taking the project beyond the minimum requirements to better demonstrate my engineering approach. This included:
  - Project setup and environment configuration.
  - Debugging and deployment issues encountered during development.
  - Setting up automated CI/CD and cloud deployments.
  - Expanding automated testing.
  - Refining the UI/UX and overall user experience.
<<<<<<< HEAD
  - Writing comprehensive documentation, including a detailed README and local setup instructions.
=======
  - Writing comprehensive documentation, including a detailed README.
>>>>>>> origin/main
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
AI was used as a productivity and engineering review tool to accelerate development while ensuring I remained responsible for all implementation decisions.

Throughout the project, I used AI to:

- Brainstorm and challenge design decisions before implementation.
- Generate configuration snippets and boilerplate where appropriate.
- Accelerate front-end styling and UI refinement.
- Suggest additional test cases and identify potential edge cases.
- Review code for opportunities to improve readability, robustness, and maintainability.

I intentionally **accepted** suggestions that kept the solution simple, production-ready, and aligned with good software engineering principles. I **rejected** suggestions that unnecessarily increased complexity or expanded the project beyond the intended scope of the assessment.

The primary tools used were **ChatGPT** for engineering discussions, code review, configuration assistance, and UI refinement, **Cursor** for selective development assistance and **CodeRabbit** for pull request and code review.

The area where AI was used the least was the **backend implementation and business logic**, as this is one of my strongest technical areas. The API design, validation, calculations, and overall backend architecture were implemented by myself, with AI serving primarily as a reviewer rather than the author of the solution.

All AI-generated suggestions were reviewed, understood, and adapted before being incorporated into the project.
<br><br>

## What I Would Do With More Time
If given additional time, I would continue evolving the application from a retirement calculator into a more comprehensive retirement planning platform. Potential future enhancements include:

- Explored the use of a tool like **Playwright** for full end-to-end testing.
- AI-powered retirement planning assistance capable of explaining projections, answering retirement-related questions, and suggesting ways to achieve different financial goals.
- More comprehensive front-end and back-end automated test coverage, including end-to-end browser testing.
- User authentication and personal accounts.
- Persistent storage of retirement plans and calculation history.
- Monthly portfolio tracking, allowing users to record actual balances and contributions over time and compare them against projections.
- Historical dashboards and long-term retirement progress tracking.
- Goal comparison tools that allow users to compare multiple retirement scenarios side-by-side.
- More advanced financial modelling, including salary growth, increasing contribution strategies, employer contributions, investment fees, taxation, configurable inflation, and different investment return assumptions.
- Educational resources integrated into the platform, including curated articles, videos, and external resources to help users better understand retirement planning and investing.
- A directory of financial advisors or retirement specialists, allowing users to transition from planning to seeking professional guidance where appropriate.
- Scenario planning tools that let users instantly explore questions such as *"What if I retire two years earlier?"* or *"What if I increase my monthly contribution by R500?"*
- Support for multiple retirement products and investment portfolios, allowing users to model different savings strategies within a single application.
<br><br>

## Additional Screenshots Of Working Application
<img width="1662" height="981" alt="image" src="https://github.com/user-attachments/assets/da0d5dfe-33a8-4d2b-a4e2-0ee3221765ee" />
<br><br>
<img width="1668" height="984" alt="image" src="https://github.com/user-attachments/assets/b955e4a2-4ff7-484e-ae51-a971cd199892" />


