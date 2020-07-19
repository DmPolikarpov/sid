
/*build line chart of shares prices for a company*/
var ctx = document.getElementById('myChart').getContext('2d');
var shares_info = new Chart(ctx, {
    type: 'line',
    data: {
        labels:[{% for share in shares %}'{{ share.trading_date }}', {% endfor %}],
        datasets: [{
            label:"Варианты отелей на выбранную дату",
            data:[{% for share in shares %}{{ share.close_price }}, {% endfor %}],
            borderColor: "#3e95cd",
        }]
    },
    options: {
        scales:{
            yAxes:[{
                ticks:{
                    beginAtZero: true
                },
            }],
        },
    },
});