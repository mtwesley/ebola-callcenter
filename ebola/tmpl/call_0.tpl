
{% extends "layout.tpl" %}

{% block content_a %}
<div class="agent_instruction text_a">
    Please read the following dialogue:
</div>

<div class="agent_dialogue text_c rounded">
    {% call dialog() %}{% endcall %}
</div>

<div class="agent_input">
<form id="form" method="POST">
    {% call input() %}
    <a class="btn gradient_green rounded" onclick="form.submit();" href="javascript:void()">
        {% if submit_label %} {{ submit_label }} {% else %} SUBMIT {% endif %}
    </a>
    {% endcall %}
</form>
</div>
<div class="agent_cancel">
    {% call cancel() %}{% endcall %}
</div>
{% endblock content_a %}

{% block content_b %}

<div class="info_title text_a"> Call Info </div>
<div class="info_content text_b">
    <span style="color:#7D7D7D;">Caller Phone:</span> {{ session.get('msisdn', 'Unknown') }}
    <br>
    
    
    <span style="color:#7D7D7D;">Caller Name:</span> {{ session.get('name', 'Unknown') }}
    <br>
    
    <span style="color:#7D7D7D;">Caller Sex:</span> {{ session.get('sex', 'Unknown') }}
    <br>
    
    <span style="color:#7D7D7D;">Caller Age:</span> {{ session.get('age', 'Unknown') }}
    <br>
    
    <span style="color:#7D7D7D;">Caller Language:</span> {{ session.get('lang', 'Unknown') }}
    <br>
    
    <span style="color:#7D7D7D;">Caller County:</span> {{ session.get('county', 'Unknown') }}
    <br>
    
    <span style="color:#7D7D7D;">Caller City:</span> {{ session.get('city', 'Unknown') }}
    <br>
    
    <span style="color:#7D7D7D;">Caller Location:</span> {{ session.get('location', 'Unknown') }}
    <br>
    
    <span style="color:#7D7D7D;">Call Type:</span> {{ session.get('call_type', 'Unknown') }}
    
</div>
<div class="info_title text_a">
    Patient Report Info
</div>
<div class="info_content text_b">
    <span style="color:#7D7D7D;">Patient Name:</span> 0886670426
    <br>
    <span style="color:#7D7D7D;">Patient Phone:</span> Charles D. Cooper
    <br>
    <span style="color:#7D7D7D;">Patient Sex:</span> Male
    <br>
    <span style="color:#7D7D7D;">Patient Age:</span> 35
    <br>
    <span style="color:#7D7D7D;">Patient Language:</span> English
    <br>
    <span style="color:#7D7D7D;">Patient County:</span> Montserrado
    <br>
    <span style="color:#7D7D7D;">Patient City:</span> Virginia
    <br>
    <span style="color:#7D7D7D;">Patient Location:</span> Hotel Africa Road
    <br>
    <span style="color:#7D7D7D;">Patient Condition:</span> Unconscious
    <br>
    <span style="color:#7D7D7D;">Ebola Contact:</span> Yes
    <br>
    <span style="color:#7D7D7D;">Symptoms Duration:</span> 2 days
    <br>
    <span style="color:#7D7D7D;">Symptoms:</span> Rash, Fever, Diarrhea, Headache, Bleeding
    <br>
    <span style="color:#7D7D7D;">Comments:</span> There are three people living in the house with the patient.
</div>
{% endblock content_b %}

{% block module_c %}
<div id="module_b" class="rounded">
    <div class="caller_related_cases text_a">
        This caller previously reported the following case(s):
        <br><br>
        {% for patient in session.patients %}
        <a class="btn2 gradient_gray3 rounded text_d" href="">
            Patient ID {{ patient.id }} {{ patient.name }}
        </a>
        {% endfor %}
        
    </div>
</div>
<div id="module_c" class="rounded">
    <div class="caller_frequency_today text_a">
        This caller has previously called <span style="color:#7D7D7D;">0</span> times today.  
    </div>
</div>
{% endblock module_c %}