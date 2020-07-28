/*
*    main.js
*    Mastering Data Visualization with D3.js
*    Project 2 - Gapminder Clone
*/

flag = false;

// Canvas
var margin = { left: 100, right: 10, top: 10, bottom: 100 };
var w = 600 - margin.left - margin.right;
var h = 400 - margin.top - margin.bottom;

var canvas = d3.select("#chart-area")
	.append("svg")
	.attr("width", w + margin.left + margin.right)
	.attr("heiht", h + margin.top + margin.bottom);

var g = canvas.append(g)
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Labels


// Scales
var x = d3.scaleBand()
	.range([0, w])
	.paddingInner(0.1)
	.paddingOuter(0.3);

var y = d3.scaleLinear()
	.range([h, 0]);

// Axis
var xAxisGroup = g.append("g")
	.attr("class", "x axis")
	.attr("transform", "translate(0," + h + ")");

var yAxisGroup = g.append("g")
	.attr("class", "y axis");


d3.json("data/data.json").then(function (data) {
	data.forEach(dtp => {
		dtp.year = +dtp.year;
	});
	console.log(data);

	d3.interval(() => {
		update(data);
		flag = !flag;
	}, 1000);
}).catch(error => console.log(error));

function update(data) {

}