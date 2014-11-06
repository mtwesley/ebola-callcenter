

{% macro dialog() -%}
    please state your Phone Number.
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
    <input type="text" name="msisdn" placeholder="Callers Phone No">
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
<a class="btn gradient_red rounded" href="{{ url_for('_ui.index') }}">
    CANCEL CALL
</a>
{{ caller() }}
{%- endmacro %}


{% include "call_0.tpl" %}

