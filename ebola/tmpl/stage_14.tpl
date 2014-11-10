


{% macro dialog() -%}
    What county are you calling from?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
{% include "counties.tpl" %}
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
<a class="btn gradient_red rounded" href="{{ url_for('_ui.index') }}">
    CANCEL CALL
</a>
{{ caller() }}
{%- endmacro %}


{% include "call_0.tpl" %}

