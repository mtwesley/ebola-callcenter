
{% extends "layout.tpl" %}

{% block hdr %}
<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script type="text/javascript">
    google.load("visualization", "1", {packages:["corechart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {

    var data = google.visualization.arrayToDataTable([
      ['Type', 'Number'],
      ['New cases',     102],
      ['Case inquiries',      58],
      ['General inquiries',  125],
      ['Duplicate cases', 43],
      ['Cancelled calls',    37]
    ]);

    var options = {
        legend: 'none',
        colors:['#B44D54','#68ACBA','#7C5866','#E3BB56','#6EAB61']
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);
    }
</script>
{% endblock hdr %}

{% block content_a %}
<div class="agent_instruction text_c">
    Click here to begin recording a new call.
</div>

<div class="agent_input">
    <a href="{{ url_for('_ui.new_call') }}" class="btn gradient_green rounded">NEW CALL</a>
</div>

{% endblock content_a %}


{% block content_b %}    
<div class="caller_related_cases text_a">
    Incoming call history
    <br><br>
    <a class="btn2 gradient_gray3 rounded text_d" href="">
        <div class="call_type" style="background:#B44D54"></div>  0886670426   Charles Cooper
    </a>
    <a class="btn2 gradient_gray3 rounded text_d" href="">
        <div class="call_type" style="background:#68ACBA"></div>  0886670426   Charles Cooper
    </a>
    <a class="btn2 gradient_gray3 rounded text_d" href="">
        <div class="call_type" style="background:#7C5866"></div>  0886670426   Charles Cooper
    </a>
    <a class="btn2 gradient_gray3 rounded text_d" href="">
        <div class="call_type" style="background:#E3BB56"></div>  0886670426   Charles Cooper
    </a>
    <a class="btn2 gradient_gray3 rounded text_d" href="">
        <div class="call_type" style="background:#6EAB61"></div>  0886670426   Charles Cooper
    </a>
</div>
{% endblock content_b %}


{% block content_c %}
<div class="agent_stats text_a">
    Your statistics today
    <div id="piechart" style="width: 280px; height: 280px;"></div>
    <div class="call_type2" style="background:#464646"></div>  355 Total calls
    <br>
    <div class="call_type2" style="background:#B44D54"></div>  102 New cases
    <br>
    <div class="call_type2" style="background:#68ACBA"></div>  58 Case inquiries
    <br>
    <div class="call_type2" style="background:#7C5866"></div>  125 General inquiries
    <br>
    <div class="call_type2" style="background:#E3BB56"></div>  43 Duplicate cases
    <br>
    <div class="call_type2" style="background:#6EAB61"></div>  27 Cancelled calls
</div>
{% endblock content_c %}