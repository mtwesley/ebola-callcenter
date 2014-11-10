


{% macro dialog() -%}
     What city is {{ session.p_name or "the patient" }} in?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<input type="text" name="city" placeholder="Patient's City Name">
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

