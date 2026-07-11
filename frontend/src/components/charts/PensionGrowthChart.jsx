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
  
      labels: projection.map(
        (item) => item.age
      ),
  
  
      datasets: [
  
        {
          label: "Your Contributions",
  
          data: projection.map(
            (item) => item.contributions
          ),
  
          fill: true,
  
          tension: 0.4,
  
          borderWidth: 2,
  
          borderColor: "#3b82f6",
  
          backgroundColor: "rgba(59, 130, 246, 0.2)",
        },
  
  
        {
          label: "Investment Growth",
  
          data: projection.map(
            (item) => item.growth
          ),
  
          fill: true,
  
          tension: 0.4,
  
          borderWidth: 2,
  
          borderColor: "#22c55e",
  
          backgroundColor: "rgba(34, 197, 94, 0.2)",
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
  
  
            title: (items) => {
  
              return `Age ${items[0].label}`;
  
            },
  
  
            label: () => {
  
              return "";
  
            },
  
  
            afterBody: (items) => {
  
              const index = items[0].dataIndex;
  
              const point = projection[index];
  
  
              return [
  
                `Total Portfolio: ${formatCurrency(point.balance)}`,
  
                `Your Contributions: ${formatCurrency(point.contributions)}`,
  
                `Investment Growth: ${formatCurrency(point.growth)}`,
  
              ];
  
            },
  
  
          },
  
        },
  
      },
  
  
      scales: {
  
  
        y: {
  
          stacked: true,
  
          ticks: {
  
            callback: (value) =>
              formatCurrency(value),
  
          },
  
        },
  
  
        x: {
  
          stacked: true,
  
          title: {
  
            display: true,
  
            text: "Age",
  
          },
  
        },
  
      },
  
    };
  
  
  
    return (
  
      <div className="h-96 w-full">
  
        <Line
          data={chartData}
          options={chartOptions}
        />
  
      </div>
  
    );
  
  }
  
  
  export default PensionGrowthChart;