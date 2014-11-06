
{% macro dialog() -%}
    Are you male or female?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="sex">
    <option>SELECT GENDER</option>
    <option value="none">None</option>
    <option value="Male">Male</option>
    <option value="Female">Female</option>
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

