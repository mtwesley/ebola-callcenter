


{% macro dialog() -%}
     What is your question?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<textarea name="question" rows="10" cols="30">

</textarea>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

