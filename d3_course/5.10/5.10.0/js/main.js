/*
*    main.js

*    Mastering Data Visualization with D3.js
*    Project 2 - Gapminder Clone
*/
var time = 0;
// Canvas
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
var tLabel = g.append("text")
	.attr("class", "x axis-label")
	.attr("x", w - 40)
	.attr("y", h - 10)
	.attr("font-size", "20px")
	.attr("text-anchor", "middle")
	.text("1800");

var xLabel = g.append("text")
    .attr("class", "x axis-label")
    .attr("x", w / 2)
    .attr("y", h + 100)
    .attr("font-size", "20px")
    .attr("text-anchor", "middle")
    .text("GDP per Capita");

var yLabel = g.append("text")
    .attr("class", "y axis-label")
    .attr("x", - (h / 2))
    .attr("y", -60)
    .attr("font-size", "20px")
    .attr("text-anchor", "middle")
	.attr("transform", "rotate(-90)")
	.text("Life Expectancy");
// Scales
var x = d3.scaleLog()
	.range([0, w])
	.domain([300, 150000])
	.base(10);

var y = d3.scaleLinear()
	.range([h, 0])
	.domain([0, 90]);

var area = d3.scaleLinear()
	.range([25* Math.PI, 25 * 25 * Math.PI])
	.domain([2000, 140000000]);

var color = d3.scaleOrdinal(d3.schemePastel2);
// Axis
var xAxis = d3.axisBottom(x)
	.tickValues([400, 4000, 40000])
	.tickFormat(d3.format("$"));
g.append("g")
	.attr("class", "x axis")
	.attr("transform", "translate(0," + h + ")")
	.call(xAxis);

var yAxis = d3.axisLeft(y)
	.tickFormat(dtp => +dtp);
g.append("g")
	.attr("class", "y axis")
	.call(yAxis);

// LEGEND

var continents = ["europe", "asia", "oceania", "africa"];

var legend = g.append("g")
	.attr("transform", "translate(" + (w - 10) + "," + (h - 150) + ")");

continents.forEach(function (cnt, i) {
	var lRow = legend.append("g")
		.attr("transform", "translate(0," + (i * 20) + ")");

	lRow.append("rect")
		.attr("width", 10)
		.attr("height", 10)
		.attr("fill", color(cnt));

	lRow.append("text")
		.attr("x", -10)
		.attr("y", 10)
		.attr("text-anchor", "end")
		.style("text-transform", "capitalize")
		.text(cnt);
})

d3.json("data/data.json").then(function (data) {
	// console.log(data);

	const clean_data = data.map(y_dtp => {
		return y_dtp['countries'].filter(c_dtp => {
			return (c_dtp.income && c_dtp.life_exp);
		}).map(c_dtp => {
			c_dtp.income = +c_dtp.income;
			c_dtp.life_exp = +c_dtp.life_exp;
			return c_dtp;
		})
	});
	// console.log(clean_data);

	d3.interval(() => {
		time = (time < 214) ? time + 1 : 0;
		update(clean_data[time]);
	}, 100);
}).catch(error => console.log(error));

function update(data) {
	var t = d3.transition()
		.duration(100);

	var circles = g.selectAll("circle")
		.data(data, dtp => dtp.country);

	circles
		.exit()
		.attr("class", "exit")
		.remove();

	circles
		.enter()
		.append("circle")
		.attr("class", "enter")
		.attr("fill", dtp => color(dtp.continent))
		.merge(circles)
		.transition(t)
		.attr("cx", dtp => x(dtp.income))
		.attr("cy", dtp => y(dtp.life_exp))
		.attr("r", dtp => Math.sqrt(area(dtp.population) / Math.PI));

	tLabel.text(+(time + 1800));
}
