{% macro dialog() -%}
     What county is {{session.p_name or "the patient’s"}} in?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
{% include "counties.tpl" %}
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

