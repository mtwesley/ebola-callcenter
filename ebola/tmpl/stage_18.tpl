


{% macro dialog() -%}
    Are you calling with a general question?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="is_general">
    <option>A General Query</option>
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

