


{% macro dialog() -%}
    Thank you for calling this case has already been reported and appropriate action is being taken. Please call again if you have any new information.
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

