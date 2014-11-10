


{% macro dialog() -%}
     What is {{ session.p_name or "the patient’s" }} primary language?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="p_lang">
    <option value="English">English</option>
    <option value="Kisi">Kisi </option>
    <option value="Manding">Manding</option>
    <option value="Kru">Kru</option>
    <option value="Gola">Gola</option>
</select>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
{{ caller() }}
{%- endmacro %}

{% include "call_0.tpl" %}

