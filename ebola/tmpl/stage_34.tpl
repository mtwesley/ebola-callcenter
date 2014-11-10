


{% macro dialog() -%}
    Has {{ session.p_name or "the patient"}} had contact with a known Ebola case?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="ebola_contact">
    <option>Ebola Contact?</option>
    <option value="Y">Yes</option>
    <option value="N">No / UnKnown</option>
</select>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}
