


{% macro dialog() -%}
    What city are you calling from?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<input type="text" name="city" placeholder="Caller City Name">
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
<a class="btn gradient_red rounded" href="{{ url_for('_ui.index') }}">
    CANCEL CALL
</a>
{{ caller() }}
{%- endmacro %}


{% include "call_0.tpl" %}

