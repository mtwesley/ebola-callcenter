


{% macro dialog() -%}
    Are you calling about {{ tmp_p_name or "" }} from {{ tmp_p_location or "Unknown" }} ?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="p_is_found">
    <option value="none">Calling For this Patient</option>
    <option value="Y">Yes</option>
    <option value="N">No</option>
</select>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}
