


{% macro dialog() -%}
     How old is {{ session["p_name"] or "the patient’s" }}
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<input type="text" name="p_age" placeholder="Patient's Age">
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

