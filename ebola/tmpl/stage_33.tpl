


{% macro dialog() -%}
     Is {{ session.p_name or "the patient"}}  awake or unconscious?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="p_status">
    <option value="N">Unknown</option>
    <option value="A">Awake</option>
    <option value="U">UnConscious</option>
</select>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

