$( document ).ready(function() {
	
	var provincias_israel = ['Upper Galilee','Golan Heights','Galilee','Judean Hills','Samson','Galil','Jerusalem Hills',
						'Shomron','Haut-Judeé','Negev','Dan','Israel','Negev Hills','Ella Valley']
	
	var showLoader = function() {
		$("#progressMaintenance2").css("display","block");
		$("#subPage").css("opacity","0.3");
		$("#subPage").css("pointer-events","none");
		$(".visible").css("visibility","hidden");
	}

	var hideLoader = function() {
		$("#progressMaintenance2").css("display","none");
		$("#subPage").css("opacity","1");
		$("#subPage").css("pointer-events","auto");
		$(".visible").css("visibility","visible");
	}
	
	
	//###############################
	//## FUNCIONALIDAD DE GRAFICAS ##
	//###############################
	
	var pieChart = function(data, id) {
		
		//Donut chart example
		nv.addGraph(function() {
		  var chart = nv.models.pieChart()
			  .x(function(d) { return d.label })
			  .y(function(d) { return d.value })
			  .showLabels(true)     //Display pie labels
			  .labelThreshold(.05)  //Configure the minimum slice size for labels to show up
			  .labelType("value") //Configure what type of data to show in the label. Can be "key", "value" or "percent"
			  .donut(true)          //Turn on Donut mode. Makes pie chart look tasty!
			  .donutRatio(0.35)     //Configure how big you want the donut hole size to be.
			  ;
			d3.select("#"+id+" svg")
				.datum(data)
				.transition().duration(350)
				.call(chart);
		  return chart;
		});
	};
	
	var barChartHorizontal = function(data, id){
		nv.addGraph(function() {
		var chart = nv.models.multiBarHorizontalChart()
			.x(function(d) { return d.label })
			.y(function(d) { return d.value })
			.margin({top: 30, right: 20, bottom: 50, left: 175})
			.showValues(true)           //Show bar value next to each bar.
			.tooltips(true)             //Show tooltips on hover.
			.transitionDuration(350)
			.showControls(true);        //Allow user to switch between "Grouped" and "Stacked" mode.

		chart.yAxis
			.tickFormat(d3.format(',.2f'));

		d3.select('#'+id+' svg')
			.datum(data)
			.call(chart);

		nv.utils.windowResize(chart.update);

		return chart;
	  });
	}
	
	var multiChart = function(data, id) {
		nv.addGraph(function() {
		  var chart = nv.models.scatterChart()
						.showDistX(true)    //showDist, when true, will display those little distribution lines on the axis.
						.showDistY(true)
						.transitionDuration(350)
						.color(d3.scale.category10().range());

		  //Configure how the tooltip looks.
		  chart.tooltipContent(function(key, x, y, size) {
			  return '<h5>' + "Pais: "+ key + " <br/> Provincia: " + provincias_israel[y-1] +
			  " <br/> Calidad: " + size.point.size +" puntos "+
			  "<br/> Precio: " + x + "$" +
			  '</h5>';
		  });

		  //Axis settings
		  chart.xAxis.tickFormat(d3.format('.02f'));
		  chart.yAxis.tickFormat(d3.format('.02f'));

		  //We want to show shapes other than circles.
		  chart.scatter.onlyCircles(false);

		  var myData = data;
		  d3.select('#'+id+' svg')
			  .datum(myData)
			  .call(chart);

		  nv.utils.windowResize(chart.update);

		  return chart;
		});
	};
	
	
	
	var wordCloud = function(texto, id) {
		var lines = texto.split(/[,\." ]+/g),
		data = Highcharts.reduce(lines, function (arr, word) {
			var obj = Highcharts.find(arr, function (obj) {
				return obj.name === word;
				
			});
			if (obj) {
				obj.weight += 1;
			} else {
				obj = {
					name: word,
					weight: 1
				};
				arr.push(obj);
			}
			return arr;
		}, []);

		Highcharts.chart(id, {
			series: [{
				type: 'wordcloud',
				data: data,
				name: 'Repeticiones',
				turboThreshold:5000
			}],
			title: {
				text: 'Palabras mas usadas para describir vinos (Israel)'
			}
		});
	};
	
	

	//#############################################
	//## LLAMADAS AJAX PARA LA CARGA DE GRAFICOS ##
	//#############################################
	
	var get_calidad_por_country = function(){
		$.ajax({
			type: "POST",
			url: "/pecDefinitiva/get_ajax_calidad_country/",
			success: function(data) {
				if (data.error !== ""){
					console.log(data.error)
				}else{
					barChartHorizontal(data.response, 'barChart');
				}
			}
		});
	};
	
	var get_precio_por_country = function(){
		$.ajax({
			type: "POST",
			url: "/pecDefinitiva/get_ajax_precio_country/",
			success: function(data) {
				if (data.error !== ""){
					console.log(data.error)
				}else{
					pieChart(data.response, "pieChart");
				}
			}
		});
	};
	
	var get_precio_por_puntuacion = function(){
		$.ajax({
			type: "POST",
			url: "/pecDefinitiva/get_ajax_precio_puntuacion/",
			success: function(data) {
				if (data.error !== ""){
					console.log(data.error)
				}else{
					barChartHorizontal(data.response, 'barChart2');
				}
			}
		});
	};
	
	var get_vinos_por_pais = function(){
		$.ajax({
			type: "POST",
			url: "/pecDefinitiva/get_ajax_vinos_pais/",
			success: function(data) {
				if (data.error !== ""){
					console.log(data.error)
				}else{
					pieChart(data.response, 'pieChart2');
				}
			}
		});
	};
	
	var get_calidad_precio = function(){
		$.ajax({
			type: "POST",
			url: "/pecDefinitiva/get_ajax_calidad_precio/",
			success: function(data) {
				if (data.error !== ""){
					console.log(data.error)
				}else{
					multiChart(data.response, 'multiChart');
				}
			}
		});
	};
	
	var get_description_wordcloud = function(){
		showLoader();
		$.ajax({
			type: "POST",
			url: "/pecDefinitiva/get_ajax_description/",
			success: function(data) {
				if (data.error !== ""){
					console.log(data.error)
				}else{
					wordCloud(data.response, 'wordCloud');
					hideLoader();
				}
			}
		});
	};
	
	
	//################################
	//## INICIALIZACION DE GRAFICOS ##
	//################################
	get_calidad_por_country();
	get_precio_por_country();
	get_precio_por_puntuacion();
	get_vinos_por_pais();
	get_calidad_precio();
	get_description_wordcloud();
	
});