/*
*    main.js
*    Mastering Data Visualization with D3.js
*    2.8 - Activity: Your first visualization!
*/

// Margins
var margin = { left: 100, right: 10, top: 10, bottom: 150 };

var w = 600 - margin.left - margin.right;
var h = 400 - margin.top - margin.bottom;

var canvas = d3.select("#chart-area")
    .append("svg")
    .attr("width", w + margin.left + margin.right)
    .attr("height", h + margin.top + margin.bottom);

var g = canvas.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Labels
g.append("text")
    .attr("class", "x axis-label")
    .attr("x", w / 2)
    .attr("y", h + 110)
    .attr("font-size", "20px")
    .attr("text-anchor", "middle")
    .text("Tallest Buildings");

g.append("text")
    .attr("class", "y axis-label")
    .attr("x", - (h / 2))
    .attr("y", -60)
    .attr("font-size", "20px")
    .attr("text-anchor", "middle")
    .attr("transform", "rotate(-90)")
    .text("Height (m)");

d3.json("data/buildings.json").then(function (data) {
    // Number Conversion
    data.forEach(element => element.height = +element.height);
    console.log(data);

    // Scales
    var x = d3.scaleBand()
        .domain(data.map(dtp => dtp.name))
        .range([0, w])
        .paddingInner(0.1)
        .paddingOuter(0.3);

    var y = d3.scaleLinear()
        .domain([0, d3.max(data, dtp => dtp.height)])
        .range([h, 0]);

    // Axis
    var xAxis = d3.axisBottom(x);
    g.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + h + ")")
        .call(xAxis)
        .selectAll("text")
        .attr("y", 10)
        .attr("x", -5)
        .attr("text-anchor", "end")
        .attr("transform", "rotate(-40)");

    var yAxis = d3.axisLeft(y)
        .ticks(3)
        .tickFormat(dtp => dtp + "m");
    g.append("g")
        .attr("class", "y axis")
        .call(yAxis);

    // Bars
    var rect = g.selectAll("rect")
        .data(data)
        .enter()
        .append("rect")
        .attr("x", dtp => x(dtp.name))
        .attr("y", dtp => y(dtp.height))
        .attr("width", x.bandwidth())
        .attr("height", dtp => h - y(dtp.height));

}).catch(error => {
    console.log(error);
});