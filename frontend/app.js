// frontend/app.js

document.getElementById("run").addEventListener("click", async () => {
  const res = await fetch(http://localhost:8000/data);
  const data = await res.json();

  drawPlot(data.x, data.y);
});

function drawPlot(x, y) {
  const ctx = document.getElementById("plot").getContext("2d");

  new Chart(ctx, {
    type: "scatter",
    data: {
      datasets: [
        {
          label: "解析結果",
          data: x.map((xi, i) => ({ x: xi, y: y[i] })),
          backgroundColor: "blue"
        }
      ]
    },
    options: {
      scales: {
        x: { title: { display: true, text: "X" } },
        y: { title: { display: true, text: "Y" } }
      }
    }
  });
}
