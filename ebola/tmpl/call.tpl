
{% extends "layout.tpl" %}

{% block content_a %}
<div class="agent_instruction text_a">
    Please read the following dialogue:
</div>
<div class="agent_dialogue text_c rounded">
    Please state the name of the patient you are calling to report.
</div>

<div class="agent_input">
    <form>
        <input type="text" name="P_name_first" placeholder="PATIENT FIRST NAME">
        <input type="text" name="P_name_middle" placeholder="PATIENT MIDDLE NAME">
        <input type="text" name="P_name_last" placeholder="PATIENT LAST NAME">
        <select name="suffix">
            <option value="none">PATIENT SUFFIX</option>
            <option value="none">None</option>
            <option value="JR">Jr.</option>
            <option value="SR">Sr.</option>
        </select>
        <a class="btn gradient_green rounded" href="">
            SUBMIT
        </a>
    </form>
</div>
<div class="agent_cancel">
    <a class="btn gradient_red rounded" href="{{ url_for('_ui.index') }}">
        CANCEL CALL
    </a>
</div>
{% endblock content_a %}

{% block content_b %}
<div class="info_title text_a"> Call Info </div>
<div class="info_content text_b">
    <span style="color:#7D7D7D;">Caller Phone:</span> 0886670426
    <br>
    <span style="color:#7D7D7D;">Caller Name:</span> Charles D. Cooper
    <br>
    <span style="color:#7D7D7D;">Caller Sex:</span> Male
    <br>
    <span style="color:#7D7D7D;">Caller Age:</span> 35
    <br>
    <span style="color:#7D7D7D;">Caller Language:</span> English
    <br>
    <span style="color:#7D7D7D;">Caller County:</span> Montserrado
    <br>
    <span style="color:#7D7D7D;">Caller City:</span> Virginia
    <br>
    <span style="color:#7D7D7D;">Caller Location:</span> Hotel Africa Road
    <br>
    <span style="color:#7D7D7D;">Call Type:</span> New Case Report
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
        <a class="btn2 gradient_gray3 rounded text_d" href="">
            Patient ID 012586  Charles Cooper
        </a>
        <a class="btn2 gradient_gray3 rounded text_d" href="">
             Patient ID 587825  James Johnson
        </a>
    </div>
</div>
<div id="module_c" class="rounded">
    <div class="caller_frequency_today text_a">
        This caller has previously called <span style="color:#7D7D7D;">5</span> times today.  
    </div>
</div>
{% endblock module_c %}