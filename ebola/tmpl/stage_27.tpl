


{% macro dialog() -%}
    Is {{ session["p_name"] or "the patient" }} Male or Female?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="p_sex">
    <option value="none">SEX</option>
    <option value="M">Male</option>
    <option value="F">Female</option>
</select>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

