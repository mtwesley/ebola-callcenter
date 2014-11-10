


{% macro dialog() -%}
    Does {{ session.p_name or "the patient"}} have any of these symptoms?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<input type="checkbox" name="symptoms" value="Fever">Fever<br/>
<input type="checkbox" name="symptoms" value="headache">headache<br/>
<input type="checkbox" name="symptoms" value="loss of appetitie">loss of appetitie<br/>
<input type="checkbox" name="symptoms" value="vomiting">vomiting<br/>
<input type="checkbox" name="symptoms" value="nausea">nausea<br/>
<input type="checkbox" name="symptoms" value="muscle pains">muscle pains<br/>
<input type="checkbox" name="symptoms" value="diarrhea">diarrhea<br/>
<input type="checkbox" name="symptoms" value="weakness">weakness<br/>
<input type="checkbox" name="symptoms" value="difficulty breathing">difficulty breathing<br/>
<input type="checkbox" name="symptoms" value="sore throat">sore throat<br/>
<input type="checkbox" name="symptoms" value="hiccups">hiccups<br/>
<input type="checkbox" name="symptoms" value="difficulty swallowing">difficulty swallowing<br/>
<input type="checkbox" name="symptoms" value="abdominal pain">abdominal pain<br/>
<input type="checkbox" name="symptoms" value="unexplained bleeding">unexplained bleeding<br/>
<input type="checkbox" name="symptoms" value="red eyes">red eyes<br/>
<input type="checkbox" name="symptoms" value="skin rash">skin rash<br/>
<input type="checkbox" name="symptoms" value="black stool">black stool<br/>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

