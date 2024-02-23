
function fetchDataAndUpdateChart() {
  fetch('/get_datachart')
      .then(response => response.json())
      .then(data => {
          updateChart(data);
      })
      .catch(error => console.error('Error:', error));
}

function updateChart(data) {
am5.ready(function() {
    var root = am5.Root.new("chartdiv");
    root.setThemes([
        am5themes_Animated.new(root),
    ]);

    var chart = root.container.children.push(
        am5percent.PieChart.new(root, {
            layout: root.verticalHorizontal
        })
    );

    // Create series
    var series = chart.series.push(
        am5percent.PieSeries.new(root, {
            name: "Series",
            valueField: "value", // Assuming the field is named "sales"
            categoryField: "class"
        })
    );
    series.data.setAll(data);

    // Add legend
    var legend = chart.children.push(am5.Legend.new(root, {
        centerX: am5.percent(50),
        x: am5.percent(50),
        layout: root.horizontalLayout
    }));

    legend.data.setAll(series.dataItems);
});
}

document.addEventListener('DOMContentLoaded', function() {
fetchDataAndUpdateChart();
});



