

{% macro dialog() -%}
    Please state your name.
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<input type="text" name="name_first" placeholder="FIRST NAME" value="{{ session.get('first_name', '') }}">
<input type="text" name="name_middle" placeholder="MIDDLE NAME" value="{{ session.get('middle_name','') }}">
<input type="text" name="name_last" placeholder="LAST NAME" value="{{ session.get('last_name','') }}">
<select name="suffix">
    <option value="none">SUFFIX</option>
    <option value="none">None</option>
    <option value="JR">Jr.</option>
    <option value="SR">Sr.</option>
</select>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
<a class="btn gradient_red rounded" href="{{ url_for('_ui.index') }}">
    NO
</a>
{{ caller() }}
{%- endmacro %}


{% include "call_0.tpl" %}

