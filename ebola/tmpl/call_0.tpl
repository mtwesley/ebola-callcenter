
{% extends "layout.tpl" %}

{% set caller = session.get('caller', None) %}
{% set p = session.get('patient', None) %}

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
    <span style="color:#7D7D7D;">Caller Phone:</span> {{ session.msisdn or 'Unknown' }}
    <br>
    
    
    <span style="color:#7D7D7D;">Caller Name:</span> {{ session.name or 'Unknown' }}
    <br>
    
    <span style="color:#7D7D7D;">Caller Sex:</span> {{ session.sex or 'Unknown' }}
    <br>
    
    <span style="color:#7D7D7D;">Caller Language:</span> {{ session.lang or 'Unknown' }}
    <br>
    
    <span style="color:#7D7D7D;">Caller County:</span> {{ session.county or 'Unknown' }}
    <br>
    
    <span style="color:#7D7D7D;">Caller City:</span> {{ session.city or 'Unknown'}}
    <br>
    
    <span style="color:#7D7D7D;">Caller Location:</span> {{ session.location or 'Unknown' }}
    <br>
    
    <span style="color:#7D7D7D;">Call Type:</span> {{ session.call_type or 'Unknown'}}
    
</div>
<div class="info_title text_a">
    Patient Report Info
</div>
<div class="info_content text_b">
    <span style="color:#7D7D7D;">Patient Name:</span> {{ session.p_name or 'Unknown'}}
    <br>
    <span style="color:#7D7D7D;">Patient Phone:</span> {{session.p_msisdn or 'Unknown'}}
    <br>
    <span style="color:#7D7D7D;">Patient Sex:</span> {{session.p_sex or 'Unknown'}}
    <br>
    <span style="color:#7D7D7D;">Patient Age:</span> {{session.p_age or 'Unknown'}}
    <br>
    <span style="color:#7D7D7D;">Patient Language:</span> {{session.p_lang or 'Unknown'}}
    <br>
    <span style="color:#7D7D7D;">Patient County:</span> {{session.p_county or 'Unknown'}}
    <br>
    <span style="color:#7D7D7D;">Patient City:</span> {{session.p_city or 'Unknown'}}
    <br>
    <span style="color:#7D7D7D;">Patient Location:</span> {{session.p_location or 'Unknown'}}
    <br>
    <span style="color:#7D7D7D;">Patient Condition:</span> 
    {%- if session.p_status == "U" -%} UnConscious 
    {%- elif session.p_status == "A" -%} Awake 
    {%- else -%} Unknown
    {%- endif -%}
    <br>
    <span style="color:#7D7D7D;">Ebola Contact:</span> 
        {% if session.p_ebola_contact == "Y" %} Yes {%else%} No/Unknown {% endif %}
    <br>
    <span style="color:#7D7D7D;">Symptoms Duration:</span>
    {% if session.p_sick_days -%} {{session.p_sick_days}} Days
    {%else%} Unknown
    {%endif%}
    <br>
    <span style="color:#7D7D7D;">Symptoms:</span> 
        {{ (session.p_symptoms or [{'symptom':'Unknown'}])|join(', ', attribute='symptom') }}
    <br>
    <span style="color:#7D7D7D;">Comments:</span> 
    {{ session.p_comment or 'Unknown'}}
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