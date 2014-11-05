
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="Author" content="" />
        <meta name="Description" content="" />
        <meta name="keywords" content="callcenter">
        <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
        <title>callcenter</title>
        <link href="{{ url_for('static',filename='css/style.css')}}" rel="stylesheet" type="text/css">
        <link href="{{ url_for('static',filename='css/styleFORM.css')}}" rel="stylesheet" type="text/css">
        {% block hdr %} {% endblock hdr %}
    </head>
    <body>
    <div id="wrapperMAIN" class="rounded gradient_gray3">
        <div id="header" class="gradient_gray2">
            <div id="logo" class="text_a">Ebola Response Call Center</div>
            <div id="pageinfo" class="text_b white">ACTIVE CALL: PATIENT NAME</div>
            <div id="dateinfo" class="text_b">
                <span> {{ g.timestamp }} </span>  
                <span class="white">&nbsp;|&nbsp;</span>  
                <span id="timer">Timer: 00:00 </span>  
                <span class="white">&nbsp;|&nbsp;</span>  
                <a href="{{ url_for('logout') }}"><span class="white">LOG-OUT</span></a>
            </div>
        </div>
       {% block body %}
       {% endblock body %}
     </div>
    </body>
</html>