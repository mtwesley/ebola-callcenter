


{% macro dialog() -%}
     Do you have any additional comments?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<textarea name="comment" rows="10" cols="30">

</textarea>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}
