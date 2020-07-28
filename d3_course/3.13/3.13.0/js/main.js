/*
*    main.js
*    Mastering Data Visualization with D3.js
*    Project 1 - Star Break Coffee
*/

var flag = false;


var t = d3.transition().duration(750);

var margin = { left: 100, right: 10, top: 10, bottom: 100 };

var h = 400 - margin.top - margin.bottom;
var w = 600 - margin.left - margin.right;

var canvas = d3.select("#chart-area")
    .append("svg")
    .attr("width", w + margin.left + margin.right)
    .attr("height", h + margin.top + margin.bottom);

var g = canvas.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

g.append("text")
    .attr("class", "x axis-label")
    .attr("x", w / 2)
    .attr("y", h + 100)
    .attr("font-size", "20px")
    .attr("text-anchor", "middle")
    .text("Month");

var yLabel = g.append("text")
    .attr("class", "y axis-label")
    .attr("x", - (h / 2))
    .attr("y", -60)
    .attr("font-size", "20px")
    .attr("text-anchor", "middle")
    .attr("transform", "rotate(-90)");

var x = d3.scaleBand()
    .range([0, w])
    .paddingInner(0.1)
    .paddingOuter(0.3);

var y = d3.scaleLinear()
    .range([h, 0]);

var xAxisGroup = g.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + h + ")");
    // .selectAll("text")
    // .attr("y", 10)
    // .attr("x", -5)
    // .attr("text-anchor", "end")
    // .attr("transform", "rotate(-40)");

var yAxisGroup = g.append("g")
    .attr("class", "y axis");

d3.json("data/revenues.json").then(function (data) {
    data.forEach(dtp => {
        dtp.revenue = +dtp.revenue;
        dtp.profit = +dtp.profit;
    });
    console.log(data);

    d3.interval(() => {
        var n_data = flag ? data : data.slice(1);
        update(n_data);
        flag = !flag;
    }, 1000);

    update(data);
}).catch(error => console.log(error));

function update(data) {
    var value = flag ? "revenue" : "profit";

    x.domain(data.map(dtp => dtp.month));
    y.domain([0, d3.max(data, dtp => dtp[value])]);

    var xAxis = d3.axisBottom(x);
    xAxisGroup
        .transition(t)
        .call(xAxis);

    var yAxis = d3.axisLeft(y)
        .ticks(5)
        .tickFormat(dtp => dtp + "$");

    yAxisGroup
        .transition(t)
        .call(yAxis);

    // JOIN DATA w/ old elements
    var rect = g.selectAll("circle")
        .data(data, dtp => dtp.month);

    // EXIT old elements that are not present in the data
    rect.exit()
        .attr("fill", "red")
        .transition(t)
        .attr("cy", y(0))
        //.attr("height", 0)
        .remove();

    // // UPDATE
    // rect.transition(t)
    //     .attr("cx", dtp => x(dtp.month))
    //     .attr("cy", dtp => y(dtp[value]))
    //     .attr("width", x.bandwidth())
    //     .attr("height", dtp => h - y(dtp[value]));

    // ENTER
    rect.enter()
        .append("circle")
        .attr("cx", dtp => x(dtp.month) + x.bandwidth() / 2)
        .attr("cy", y(0))
        // .attr("width", x.bandwidth())
        // .attr("height", 0)
        .attr("r", 5)
        .attr("fill", "grey")
        .merge(rect)
        .transition(t)
        .attr("cx", dtp => x(dtp.month) + x.bandwidth() / 2)
        .attr("cy", dtp => y(dtp[value]));
        // .attr("width", x.bandwidth())
        // .attr("height", dtp => h - y(dtp[value]));

    var label = flag ? "Revenue" : "Profit";
    yLabel.text(label);
}