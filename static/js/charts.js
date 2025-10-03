

function rendercovidchart(canvasId, covidData, labelPrefix, charttype) {

        const ctx = document.getElementById(canvasId).getContext('2d');

    new Chart(ctx, {
        type: chartType, // "bar" or "doughnut"
        data: {
            labels: ['Cases', 'Deaths', 'Recovered'],
            datasets: [{
                label: `${labelPrefix} COVID-19 Stats`,
                data: [
                    covidData.cases || 0,
                    covidData.deaths || 0,
                    covidData.recovered || 0
                ],
                backgroundColor: [
                    '#3498db', // cases = blue
                    '#e74c3c', // deaths = red
                    '#2ecc71'  // recovered = green
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top' }
            },
            scales: chartType === 'bar' ? {
                y: {
                    beginAtZero: true
                }
            } : {} // no axes for doughnut
        }
    });
}

window.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('globalChartBar')) {
        renderCovidChart('globalChartBar', covidData, 'Global', 'bar');
    }
    if (document.getElementById('globalChartDoughnut')) {
        renderCovidChart('globalChartDoughnut', covidData, 'Global', 'doughnut');
    }
    if (document.getElementById('countryChartBar')) {
        renderCovidChart('countryChartBar', covidData, 'Country', 'bar');
    }
    if (document.getElementById('countryChartDoughnut')) {
        renderCovidChart('countryChartDoughnut', covidData, 'Country', 'doughnut');
    }
});





