
/*build data for chart of shares prices for a company*/
function getChartData(period) {
    let labels = []
    let price_data = []
    let volume_data = []
    if (period == 'one_month') {
        {% for share in shares %}
            {% if share.trading_date > one_month %}
                labels.push('{{ share.trading_date }}')
                price_data.push('{{ share.close_price }}')
                volume_data.push('{{ share.volume }}')
            {% endif %}
        {% endfor %}
        var price_label = '1 месяц'
    } else if (period == 'six_months') {
        {% for share in shares %}
            {% if share.trading_date > six_months %}
                labels.push('{{ share.trading_date }}')
                price_data.push('{{ share.close_price }}')
                volume_data.push('{{ share.volume }}')
            {% endif %}
        {% endfor %}
        var price_label = '6 месяцев'
    } else if (period == 'one_year') {
        {% for share in shares %}
            {% if share.trading_date > one_year %}
                labels.push('{{ share.trading_date }}')
                price_data.push('{{ share.close_price }}')
                volume_data.push('{{ share.volume }}')
            {% endif %}
        {% endfor %}
        var price_label = '1 год'
    } else if (period == 'five_years') {
        {% for share in shares %}
            {% if share.trading_date > five_years %}
                labels.push('{{ share.trading_date }}')
                price_data.push('{{ share.close_price }}')
                volume_data.push('{{ share.volume }}')
            {% endif %}
        {% endfor %}
        var price_label = '5 лет'
    } else if (period == 'ten_years') {
        {% for share in shares %}
            {% if share.trading_date > ten_years %}
                labels.push('{{ share.trading_date }}')
                price_data.push('{{ share.close_price }}')
                volume_data.push('{{ share.volume }}')
            {% endif %}
        {% endfor %}
        var price_label = '10 лет'
    } else if (period == 'all_time') {
        {% for share in shares %}
            labels.push('{{ share.trading_date }}')
            price_data.push('{{ share.close_price }}')
            volume_data.push('{{ share.volume }}')
        {% endfor %}
        var price_label = 'за все время'
    }

    const shareData = {
            labels: labels.sort(),
            datasets: [{
                label: price_label,
                data: price_data,
                borderColor: "#3e95cd",
                yAxisID: 'share_price',
                type: 'line'
            },
            {
                label: 'volume',
                data: volume_data,
                borderColor: "#3e95cd",
                backgroundColor: "rgb(255,0,0)",
                yAxisID: 'volume'
            }]
        }

    return shareData;
}

const options = {
    scales:{
        yAxes:[{
            ticks:{
                beginAtZero: true
            },
            position: 'left',
            display: true,
            id: 'share_price'
        },
        {
            ticks:{
                beginAtZero:true
            },
            position: 'right',
            display: true,
            id: 'volume'
        }],
    },
}

var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {type: 'bar', data: getChartData('one_year'), options: options})

document.getElementById("0").addEventListener('click', () => {
    chart.config.data = getChartData('one_month')
    chart.update();
});
document.getElementById("1").addEventListener('click', () => {
    chart.config.data = getChartData('six_months')
    chart.update();
});
document.getElementById("2").addEventListener('click', () => {
    chart.config.data = getChartData('one_year')
    chart.update();
});
document.getElementById("3").addEventListener('click', () => {
    chart.config.data = getChartData('five_years')
    chart.update();
});
document.getElementById("4").addEventListener('click', () => {
    chart.config.data = getChartData('ten_years')
    chart.update();
});
document.getElementById("5").addEventListener('click', () => {
    chart.config.data = getChartData('all_time')
    chart.update();
});