


{% macro dialog() -%}
    Does {{ session.p_name or "the patient"}} have any of these symptoms?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<input type="checkbox" name="symptoms" value="Fever">Fever
<input type="checkbox" name="symptoms" value="headache">headache
<input type="checkbox" name="symptoms" value="loss of appetitie">loss of appetitie
<input type="checkbox" name="symptoms" value="vomiting">vomiting
<input type="checkbox" name="symptoms" value="nausea">nausea
<input type="checkbox" name="symptoms" value="muscle pains">muscle pains
<input type="checkbox" name="symptoms" value="diarrhea">diarrhea
<input type="checkbox" name="symptoms" value="weakness">weakness
<input type="checkbox" name="symptoms" value="difficulty breathing">difficulty breathing
<input type="checkbox" name="symptoms" value="sore throat">sore throat
<input type="checkbox" name="symptoms" value="hiccups">hiccups
<input type="checkbox" name="symptoms" value="difficulty swallowing">difficulty swallowing
<input type="checkbox" name="symptoms" value="abdominal pain">abdominal pain
<input type="checkbox" name="symptoms" value="unexplained bleeding">unexplained bleeding
<input type="checkbox" name="symptoms" value="red eyes">red eyes
<input type="checkbox" name="symptoms" value="skin rash">skin rash
<input type="checkbox" name="symptoms" value="black stool">black stool
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

