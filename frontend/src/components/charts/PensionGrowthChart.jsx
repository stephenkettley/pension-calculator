import {
  CategoryScale,
  Chart as ChartJS,
  Filler,
  Legend,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip,
} from "chart.js";
import { Line } from "react-chartjs-2";

import { formatCurrency } from "../../utils/formatters";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
  Filler
);

function PensionGrowthChart({ projection }) {
  const chartData = {
    labels: projection.map((item) => item.age),
    datasets: [
      {
        label: "Your Contributions",
        data: projection.map((item) => item.contributions),

        borderColor: "#3b82f6",
        backgroundColor: "rgba(59, 130, 246, 0.2)",

        fill: true,
        tension: 0.4,
        borderWidth: 2,
      },
      {
        label: "Investment Growth",
        data: projection.map((item) => item.growth),

        borderColor: "#22c55e",
        backgroundColor: "rgba(34, 197, 94, 0.2)",

        fill: true,
        tension: 0.4,
        borderWidth: 2,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,

    interaction: {
      mode: "index",
      intersect: false,
    },

    plugins: {
      legend: {
        position: "top",
      },

      tooltip: {
        callbacks: {
          title: (items) => `Age ${items[0].label}`,

          afterTitle: (items) => {
            const point = projection[items[0].dataIndex];

            return `Total Portfolio: ${formatCurrency(point.balance)}`;
          },

          label: (context) => {
            const point = projection[context.dataIndex];

            return context.dataset.label === "Your Contributions"
              ? `Your Contributions: ${formatCurrency(point.contributions)}`
              : `Investment Growth: ${formatCurrency(point.growth)}`;
          },
        },
      },
    },

    scales: {
      x: {
        stacked: true,
        title: {
          display: true,
          text: "Age",
        },
      },

      y: {
        stacked: true,
        title: {
          display: true,
          text: "Amount",
        },
        ticks: {
          callback: (value) => formatCurrency(value),
        },
      },
    },
  };

  return (
    <div className="h-96 w-full">
      <Line data={chartData} options={chartOptions} />
    </div>
  );
}

export default PensionGrowthChart;