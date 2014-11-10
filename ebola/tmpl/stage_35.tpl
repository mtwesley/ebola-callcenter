


{% macro dialog() -%}
    How many days has {{ session.p_name or "the patient"}} been sick?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<input type="text" name="p_sick_days" placeholder="patient illness duration">
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

