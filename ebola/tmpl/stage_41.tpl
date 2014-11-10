


{% macro dialog() -%}
     Thank you for calling, someone will call you back shortly with an answer to your question.
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

