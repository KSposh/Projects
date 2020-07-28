/*
*    main.js
*    Mastering Data Visualization with D3.js
*    2.5 - Activity: Adding SVGs to the screen
*/

var canvas = d3.select("#chart-area")
    .append("svg")
    .attr("width", 500)
    .attr("height", 400);

var line = canvas.append("line")
    .style("stroke", "black")
    .attr("width", 20)
    .attr("x1", 0)
    .attr("y1", 0)
    .attr("x2", 20)
    .attr("y2", 30);

var rec = canvas.append("rect")
    .attr("width", 10)
    .attr("height", 30)
    .attr("x", 40)
    .attr("y", 0);

var elipse = canvas.append("ellipse")
    .attr("cx", 100)
    .attr("cy", 100)
    .attr("rx", 50)
    .attr("ry", 20);