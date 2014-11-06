


{% macro dialog() -%}
    Do you have new info about {% if patient -%} {{ patient }} {%- else -%} a reported case {%- endif%}?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="new_info">
    <option>Have New Info?</option>
    <option value="Y">Yes</option>
    <option value="N">No</option>
</select>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
<a class="btn gradient_red rounded" href="{{ url_for('_ui.index') }}">
    CANCEL CALL
</a>
{{ caller() }}
{%- endmacro %}


{% include "call_0.tpl" %}
