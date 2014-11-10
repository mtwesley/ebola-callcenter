


{% macro dialog() -%}
    What community is {{ session.p_name or "the patient" }} in?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<input type="text" name="location" placeholder="Community">
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

