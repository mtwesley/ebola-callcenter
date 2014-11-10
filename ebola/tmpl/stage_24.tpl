

{% macro dialog() -%}
    Please state the patient’s name
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<input type="text" name="p_name_first" placeholder="FIRST NAME" value="{{session.p_first_name or ''}}">
<input type="text" name="p_name_middle" placeholder="MIDDLE NAME" value="{{session.p_middle_name or ''}}">
<input type="text" name="p_name_last" placeholder="LAST NAME" value="{{ session.p_last_name or ''}}">

<select name="p_suffix">
    <option value="none">SUFFIX</option>
    <option value="none">None</option>
    <option value="JR">Jr.</option>
    <option value="SR">Sr.</option>
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

