


{% macro dialog() -%}
     What is your question?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
{%set submit_label = 'END CALL' %}
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

